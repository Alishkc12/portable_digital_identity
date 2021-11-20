from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index),
    path('new_bank_acc', views.bank),
  path('liscence_form', views.liscence),
     
]
