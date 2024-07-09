from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('homepage/', views.load_home_page,name='load_home_page'),
    
    path('features/', views.load_features,name='load_features'),
    
    path('contact us/', views.load_contact_us,name='load_contact_us'),
    
    path('aboutus/', views.load_about_us,name='load_about_us'),
    
]
