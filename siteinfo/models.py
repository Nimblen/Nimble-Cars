from django.db import models
# Create your models here.



class Message(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.CharField(max_length=150)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    user = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Message by {self.user}"







