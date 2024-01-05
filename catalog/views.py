from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from .models import Car, CarBrand, Order, Photo, Visit, Video
from .utils.paginator_utils import paginate_objects
from blog.models import Post


def index(request):
    cars = Car.objects.all()
    top_cars = Car.objects.annotate(visits_count=Count('visit')).order_by('-visits_count')[:5]
    top_posts = Post.objects.annotate(visits_count=Count('visit')).order_by('-visits_count')[:3]
    videos = Video.objects.all()
    context = {"cars": cars, 'top_cars': top_cars, 'top_posts': top_posts, 'videos': videos}
    return render(request, "catalog/index.html", context)




def catalog(request):
    sort_by = request.GET.get('sort_by', 'pk')  # значение по умолчанию - 'id'
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page', 10)
    if sort_by:
        order_cars = Car.objects.all().order_by(sort_by)
    count_of_car = Car.objects.count()
    paginated_cars = paginate_objects(order_cars, page, per_page)
    context = {
        "cars": paginated_cars,
        "car_count": count_of_car,
        "products_count": per_page,
        "page_number": page,
    }
    return render(request, "catalog/catalog.html", context)



def product(request, brand_slug, car_slug, car_id):
    brand_id = CarBrand.objects.get(name=brand_slug)
    car = get_object_or_404(Car, brand=brand_id, slug=car_slug, pk=car_id)
    photo = Photo.objects.all().filter(car_id=car_id)
    ip_address = request.META.get("REMOTE_ADDR")
    Visit.objects.create(user=request.user, ip=ip_address, car_id=car_id)
    v = Visit.objects.filter(car_id=car_id).count()
    similar_cars = Car.objects.filter(brand = brand_id)[:4]
    context = {"car": car, "visit": v, "photo": photo, "similar_cars": similar_cars}
    return render(request, "catalog/product_page.html", context)



def order_car(request, car_id):
    car = Car.objects.get(id=car_id)
    Order.objects.create(car=car, user=request.user)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))




def car_filter(request):
    # Получаем значения фильтров из запроса
    brand = int(request.GET.get("car_brand_id"))
    year_from = int(request.GET.get("car_year_from"))
    year_to = int(request.GET.get("car_year_to"))
    price_from = request.GET.get("min_price_point")
    price_to = request.GET.get("max_price_point")
    # Выполняем фильтрацию данных
    queryset = Car.objects.all()
    if brand and brand > 0:
        queryset = queryset.filter(brand=brand)
    if year_from and year_from > 0:
        queryset = queryset.filter(fabrication__gte=year_from)

    if year_to and year_to > 0:
        queryset = queryset.filter(fabrication__lte=year_to)

    if price_from and price_to:
        queryset = queryset.filter(price__gte=price_from, price__lte=price_to)

    # #Отображаем отфильтрованные данные в шаблоне
    paginated_cars = paginate_objects(queryset, page_number=1, per_page=10)
    context = {
        "cars": paginated_cars,
        "price_from": price_from,
        "price_to": price_to,
        "page_number": 1,
        "car_count": queryset.count(),
    }
    return render(
        request,
        "catalog/catalog.html",
        context,
    )

