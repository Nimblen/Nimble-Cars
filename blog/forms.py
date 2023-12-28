from django import forms
from .models import Comment


class CommentPostForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    website = forms.CharField(max_length=150)
    body = forms.Textarea()
    class Meta:
        model = Comment
        fields = ('name', 'email', 'website', 'body')


class SearchForm(forms.Form):
    query = forms.CharField()