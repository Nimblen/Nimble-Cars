from django.shortcuts import render
from blog.models import Post
from catalog.models import Car, CarBrand

# Create your views here.


def search_view(request):
    word = request.GET.get("q")
    cars = None
    articles = None
    dealers = None
    if word:
        cars = Car.objects.filter(car_model__iregex=word)
        articles = Post.objects.filter(title__iregex=word)
        dealers = CarBrand.objects.filter(name__iregex=word)
    context = {
        "title": "Результаты поиска",
        "searching_cars": cars,
        "articles": articles,
        "dealers": dealers,
    }

    return render(request, "search/results.html", context)
