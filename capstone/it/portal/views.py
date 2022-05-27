from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User, Comps, CPU, RAM, HDD, Monitor, OS
from .forms import NewCompForm


# Create your views here.

def index(request):
    return render(request, 'portal/index.html', {

    })

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
            return render(request, "portal/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "portal/login.html")


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
            return render(request, "portal/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "portal/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "portal/register.html")

   

@login_required
def invent(request):
    form = NewCompForm()
    comps = Comps.objects.all()

    if request.method == 'POST':
        form = NewCompForm(request.POST)
        if form.is_valid():
            new_comp = form.save()
            
            return redirect('invent')
        else:
            messages.error(request, 'An error occurred during registration')

    
    return render(request, 'portal/invent.html', {
        "comps": comps,
        "form": form
    })