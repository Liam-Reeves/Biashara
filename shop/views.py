from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from .models import Category, Customer, Product


# Create your views here.

def home(request):
    context ={}
    return render(request, "home.html")
def products(request):
    context ={}
    return render(request, "products.html")

def deals(request):
    context ={}
    return render(request, "deals.html")

def cart(request):
    context ={}
    return render(request, "cart.html")

def contact(request):
    context ={}
    return render(request, "contact.html")

def about(request):
    context ={}
    return render(request, "about.html")



