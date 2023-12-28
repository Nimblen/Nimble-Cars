from django import forms
from .models import Message


class AddMessageForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    website = forms.CharField(max_length=150)
    body = forms.Textarea()
    class Meta:
        model = Message
        fields = ('name', 'email', 'website', 'body')
