from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login/',views.logins,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign-up/',views.SignUp,name='sign-up'),
]
