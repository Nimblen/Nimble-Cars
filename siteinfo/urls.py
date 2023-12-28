from django.urls import path
from .views import all_dealers, dealer, contact, subscribe_email

app_name = 'dealer'

urlpatterns = [
    path('add_message/', contact, name='add_message'),
    path('add_email/', subscribe_email, name='add_email'),
    path('', all_dealers, name='dealers'),
    path('<str:name>/', dealer, name='dealer'),
]
