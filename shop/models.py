from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100, blank=False)

    email = models.EmailField(unique=True, blank=False)

    phone_number = models.CharField(max_length=100, blank=False)

    nationality =models.CharField(max_length=100, blank=False)
    
    date_of_birth = models.DateField(blank=False)
    
    gender = models.CharField(max_length=100, blank=False)

    address = models.CharField(max_length=200, blank=False)

    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.name
    
  
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    class Meta:
        verbose_name_plural = "Categories"


    def __str__ (self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False),

    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    description = models.TextField(max_length=1000, blank=True)

    image= models.ImageField(upload_to='uploads/product')

    class Meta:
        verbose_name_plural = "Products"

    def __str__ (self):
        return self.name





