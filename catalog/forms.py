from django import forms
from .models import Subscriber



class SortForm(forms.Form):
    sort_form = forms.TypedChoiceField(label='Сортировать:', choices=[('DT', 'Date'), ('PR', 'Price'), ('NM', 'Name'), ('MF', 'Manufacturer')])






class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']




