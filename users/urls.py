from django.urls import path
from .views import register, login, logout_user



app_name = 'users'

urlpatterns = [
    path('login/', login,  name='login'),
    path('register/', register,  name='register'),
    path('logout/', logout_user,  name='logout'),
]
