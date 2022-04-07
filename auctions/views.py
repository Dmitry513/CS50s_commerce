from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Commodity

from .forms import CommodityForm


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def mylisting(request):
    return render(request, 'auctions/mylisting.html')


def mybids(request):
    return render(request, 'auctions/mybids.html')


def createlisting(request):
    if request.method == 'POST':
        form = CommodityForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=int(request.user.id))
            if request.POST['image']:
                commodity = Commodity(name=request.POST['name'],
                                      description=request.POST['description'],
                                      user=user,
                                      image=request.POST['image'],
                                      startprice=int(request.POST['startprice']))
                commodity.save()
            return render(request, 'auctions/createlisting.html', {
                'form': CommodityForm,
                'message': 'Listing saved successfully!'
            })
        else:
            return render(request, 'auctions/createlisting.html', {
                'form': form
            })
    else:
        return render(request, 'auctions/createlisting.html', {
            'form': CommodityForm
        })
