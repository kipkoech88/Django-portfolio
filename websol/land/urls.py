from django.urls import path 
from django.http import HttpResponse
from django.shortcuts import render 
from . import views

urlpatterns=[ 
    path("", views.index, name='index'),
    path("about/", views.about, name="about"), 
    path("services/", views.services, name='services'), 
    path("contact/", views.contact_us, name="contact"), 
    path("sign/", views.sign_up, name="sign_up")
]