from django.contrib import admin
from django.urls import path,include
from project import views
urlpatterns = [
    path('', views.project),
]
