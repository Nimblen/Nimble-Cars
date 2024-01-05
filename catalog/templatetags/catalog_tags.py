from django import template
from django.utils.http import urlencode
from catalog.models import  Car, CarBrand, Carcase




register = template.Library()



@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

@register.simple_tag(name='all_brands')
def get_brands():
    return CarBrand.objects.all()


@register.simple_tag(name='brand_name')
def get_brands_by_id(brand_id = 1):
    try:
        return CarBrand.objects.get(id=brand_id).name
    except CarBrand.DoesNotExist:
        return 'Any'

@register.simple_tag(name='all_cases')
def get_cases():
    return Carcase.objects.all()



@register.simple_tag(name='all_cars_fabrication')
def all_cars_sort_by_fabrication():
    return Car.objects.all().order_by('fabrication')

@register.simple_tag(name='min_car_price')
def min_car_price():
    try:
        return Car.objects.all().order_by('price')[0].price - 1
    except IndexError:
        return 0

@register.simple_tag(name='max_car_price')
def max_car_price():
    try:
        return Car.objects.all().order_by('-price')[0].price + 1
    except IndexError:
        return 0


@register.simple_tag(name='list_template')
def get_list_template():
    return 'catalog/catalog_list.html'

@register.simple_tag(name='get_template')
def get_template(g = 'n'):
    if g == 'y':
        return 'catalog/catalog_grid.html'
    return 'catalog/catalog_list.html'

# @register.inclusion_tag('catalog/catalog_grid.html')
# def show_grid_layout():
#     cars = all_cars()

#     return {'cars': cars}


# @register.inclusion_tag('catalog/catalog_list.html')
# def show_list_layout():
#     cars = all_cars()
#     return {'cars': cars}


