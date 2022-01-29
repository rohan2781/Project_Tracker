from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index),
    path('login/',views.login,name='login'),
    path('admins/',views.admin,name='admin'),
    path('customer/',views.customer,name='customer'),
]
