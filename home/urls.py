from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='Services'),
    path('contact', views.contact, name='Contact Us'),
    path('services/packages', views.packages, name='Packages'),
    path('services/packages/basic1', views.basic1, name='Basic1'),
    path('work', views.work, name='Work'),
    path('services/webdev', views.webdev, name='Webdev'),


]