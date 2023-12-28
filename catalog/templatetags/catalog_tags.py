from django import template
from catalog.models import  Car, CarBrand, Carcase




register = template.Library()



@register.simple_tag(name='top_cars')
def top_cars():

    pass



@register.simple_tag(name='all_brands')
def get_brands():
    return CarBrand.objects.all()


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
