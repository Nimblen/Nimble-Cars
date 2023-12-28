from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from catalog.models import CarBrand, Car, Subscriber
from siteinfo.forms import AddMessageForm

# Create your views here.


def contact(request):
    if request.method == "POST":
        comment_form = AddMessageForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    return render(request, "siteinfo/contacts.html")


def all_dealers(request):
    dealers = CarBrand.objects.all()
    return render(request, "siteinfo/dealers.html", {"dealers": dealers})


def dealer(request, name):
    dealers = get_object_or_404(CarBrand, name=name)
    dealer_cars = Car.objects.filter(brand=dealers)
    context = {"dealer_cars": dealer_cars, "dealer": dealers}
    return render(request, "siteinfo/dealer.html", context)


def subscribe_email(request):
    email = request.GET.get("email")
    Subscriber.objects.create(email=email)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
