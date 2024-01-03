from django.urls import path
from .views import catalog, car_filter, product, order_car



app_name = 'catalog'

urlpatterns = [
    path('list/', catalog,  name='catalog_list'),
    path('grid/', catalog,  name='catalog_grid'),
    path('page/<int:page_number>/<int:per_page>/', catalog, name='paginator'),
    path('filter/', car_filter, name='filter'),
    path('<slug:brand_slug>/<slug:car_slug>/<int:car_id>/', product, name='car_detail'),
    path('order/<int:car_id>/', order_car, name='order_car'),

]
