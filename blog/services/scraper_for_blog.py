import json
import requests
from bs4 import BeautifulSoup
from blog.models import Post

path = 'blog/services/scraper_results/'

def create_post():
    res = requests.get("https://quto.ru/journal/articles")
    src = res.text

    articles_list = []
    soup = BeautifulSoup(src, "lxml")
    article_links = soup.find_all("a", class_="jsx-642473951 link QUieMngm")
    for article in article_links:
        if article is not None:
            articles_list.append(article["href"])

    for article in articles_list:
        full_url = f"https://quto.ru{article}"
        res = requests.get(full_url)
        src = res.text
        art_slug_with_slash = article.split("/")
        art_slug = art_slug_with_slash[-1].replace(".htm", "")

        with open(f"{path}links.html", "w", encoding="utf-8") as f:
            f.write(src)

        with open(f"{path}links.html", encoding="utf-8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")

        title = soup.find("h1", class_="jsx-595565450 Cqvs5c42")
        if title is not None:
            title = title.text
        else:
            title = "Title not found"
        header = soup.find("span", class_="jsx-595565450 Cqvs5c42")
        if header is not None:
            header = header.text
        else:
            header = "header not found"
        description = soup.find("div", class_="jsx-595565450 lead")
        if description is not None:
            description = description.text
        else:
            description = "description not found"

        text_list = soup.find_all("div", class_="jsx-3863504972 vikont")
        clear_text = ""
        for i in text_list:
            clear_text += i.text

        data = {
            "title": title,
            'author_id': 1,
            'slug': art_slug,
            'tags':'cars',
            # "description": description,
            # "header": header,
            "body": description + clear_text + header,
        }

        #return Post.objects.create(**data)


        with open(f"{path}{art_slug}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)


        with open(f"{path}{art_slug}.json", encoding='utf-8') as f:
            template = json.load(f)

            return Post.objects.create(**template)


