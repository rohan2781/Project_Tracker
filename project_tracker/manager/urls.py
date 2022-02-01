from django.contrib import admin
from django.urls import path
from manager import views
urlpatterns = [
    path('', views.manager),
    path('admin_client/',views.admin_client,name='admin_client'),
]
