import uuid
from users.models import CustomUser
from django.db import models
from django.urls import reverse


# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=16, unique=True)
    description = models.TextField(max_length=500)
    picture = models.ImageField(upload_to="cars_brand_images", verbose_name="Изображение")

    def get_first_photo(self):
        if self.picture:
            try:
                return self.picture.all()[0].image.url
            except IndexError:
                return "-"
        else:
            return "-"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("dealer:dealer", args=[self.name])

class Carcase(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    offer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    brand = models.ForeignKey(to=CarBrand, on_delete=models.PROTECT)
    car_model = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField()
    body_type = models.ForeignKey(to=Carcase, on_delete=models.PROTECT)
    fabrication = models.PositiveSmallIntegerField()
    max_speed = models.PositiveSmallIntegerField(default=0)
    fuel = models.CharField(max_length=16)
    engine = models.CharField(max_length=128)
    transmission = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    doors = models.CharField(max_length=16)
    co2_emissions_combined = models.CharField(max_length=32)
    features = models.CharField(max_length=128)
    other_parameters = models.CharField(max_length=128)
    safety = models.CharField(max_length=128)
    comfort = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.car_model

    def get_absolute_url(self):
        return reverse("catalog:car_detail", args=[self.brand.name, self.slug, self.pk])

    def get_first_photo(self):
        if self.images:
            try:
                return self.images.all()[0].image.url
            except IndexError:
                return "-"
        else:
            return "-"



class Photo(models.Model):
    image = models.ImageField(upload_to="cars_images", verbose_name="Изображение")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f"{self.car.car_model}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="cars_images",  null=True, blank=True)
    duration = models.DurationField()
    link = models.URLField()

    def __str__(self):
        return self.title




class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email



class Visit(models.Model):
    user = models.CharField(max_length=30, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
