import json
import requests
from bs4 import BeautifulSoup
from blog.models import Post


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
        print(article)
        full_url = f"https://quto.ru{article}"
        res = requests.get(full_url)
        src = res.text
        art_slug_with_slash = article.split("/")
        art_slug = art_slug_with_slash[-1].replace(".htm", "")

        with open("blog/services/scraper_results/links.html", "w", encoding="utf-8") as f:
            f.write(src)

        with open("blog/services/scraper_results/links.html", encoding="utf-8") as file:
            src = file.read()
            soup = BeautifulSoup(src, "lxml")

        title = soup.find("h1", class_="jsx-3076554768 Cqvs5c42").text
        header = soup.find("span", class_="jsx-3076554768 subtitle").text
        description = soup.find("div", class_="jsx-3076554768 lead").text
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


        with open(f"blog/services/scraper_results/{art_slug}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)


        with open(f"blog/services/scraper_results/{art_slug}.json", encoding='utf-8') as f:
            template = json.load(f)

            return Post.objects.create(**template)


