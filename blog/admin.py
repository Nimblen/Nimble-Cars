from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Comment
# Register your models here.



class PostAdminForm(forms.ModelForm):
    """Форма с виджетом ckeditor"""
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    form = PostAdminForm
    date_hierarchy = 'publish'
    list_editable = ['status']
    ordering = ['status', 'publish']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')