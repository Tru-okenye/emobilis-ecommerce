from django.urls import path
from . import views


app_name ="myportfolio"
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('shop/', views.shop, name="shop"),
    path('thankyou', views.thankyou, name="thankyou")
   
]