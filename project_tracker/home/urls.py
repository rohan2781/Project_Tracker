from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from home import views
urlpatterns = [
    path('', views.index),
    url(r'^login/$',views.login,name='login'),
    url(r'^admin/$',views.admin,name='admin'),
    url(r'^customer/$',views.customer,name='customer'),
]
