from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    phone_number2 = models.CharField(max_length=15, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
