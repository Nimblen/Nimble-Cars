from django.contrib import admin
from .models import Car, CarBrand, Carcase, Photo, Video, Order
# Register your models here.




@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'brand', 'body_type', 'price']
    list_filter = ['car_model', 'brand', 'body_type', 'price']
    search_fields = ['brand', 'price', 'body_type']

    prepopulated_fields = {'slug': ('car_model',)}
    #radio_fields = {'brand':admin.VERTICAL}
    #raw_id_fields = ['brand']
    ordering = ['brand', 'price']



@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Carcase)
class CarcaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration')
    list_filter = ('title', 'duration')
    search_fields = ('title',)
    ordering = ('title', 'duration')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'car')



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['car']


