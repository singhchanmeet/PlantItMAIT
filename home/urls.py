from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('social/', views.social, name='social'),
    path('plantfinder/', views.plantfinder, name='plantfinder'),
    path('searchlocation/', views.searchlocation, name='searchlocation'),
    path('searchplant/', views.searchplant, name='searchplant')
]

urlpatterns += staticfiles_urlpatterns()