"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import index
from siteinfo.views import contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('dealers/', include('siteinfo.urls', namespace='dealer')),
    path('search/', include('search.urls', namespace='search')),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('user/', include('users.urls', namespace='users')),



]

handler404 = "blog.views.page_not_found_view"
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

