from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('task/update.html/<str:pk>/', views.update, name="update"),
    path('task/delete.html/<str:pk>/', views.delete, name="delete"),
]
