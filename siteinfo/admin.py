from django.contrib import admin

from catalog.models import Subscriber
from .models import Message
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',  'created', 'user')
    list_filter = ( 'created', 'updated')
    search_fields = ('name', 'email', 'body')



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)