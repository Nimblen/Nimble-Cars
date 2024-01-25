from django.urls import path
from .views import catalog, product, order_car



app_name = 'catalog'

urlpatterns = [
    path('', catalog,  name='catalog'),
    path('<slug:brand_slug>/<slug:car_slug>/<int:car_id>/', product, name='car_detail'),
    path('order/<int:car_id>/', order_car, name='order_car'),

]
