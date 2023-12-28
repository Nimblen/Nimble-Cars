from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import CustomUser


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
    { 'placeholder':'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Введите пароль'
    }))
    remember_me = forms.BooleanField(required=False)
    class Meta:
        model = CustomUser
        fields = ('username', 'password')



class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите фамилию'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите имя пользователя'}))
    phone_number1 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите номер телефона'}))
    phone_number2 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите второй номер телефона'}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Введите пароль'}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'placeholder':'Подтвердите пароль'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'phone_number1', 'phone_number2', 'password1', 'password2')



class UserProfileForm(UserChangeForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'form-control py-4', 'readonly':True}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control py-4', 'readonly':True}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'custom-file-input'}), required=False)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'image', 'username', 'email')

