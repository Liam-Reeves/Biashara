from django.contrib import admin
from django.db import models
from .models import Customer, Category, Product

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)

