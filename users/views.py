from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserRegistrationForm, UserLoginForm
from django.urls import reverse
from django.contrib import auth, messages

# Create your views here.






def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.ip = request.META.get('REMOTE_ADDR')
            user.save()
            messages.success(request, 'Регистрация прошла успешно!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/registration.html', context)


def logout_user(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
