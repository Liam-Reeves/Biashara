from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
    path('', views.home, name="home"),

    path('products/', views.products, name= "products"),

    path('deals/', views.deals, name= "deals"),

    path('cart/', views.cart, name= "cart"),

    path('contact/', views.contact, name= "contact"),

    path('about/', views.about, name= "about"),

   
    
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)