from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from .models import Category, Customer, Product


# Create your views here.

def index(request):
    context ={}
    return render(request, "index.html")
def store(request):
    context ={}
    return render(request, "store.html")

def cart(request):
    context ={}
    return render(request, "cart.html")



