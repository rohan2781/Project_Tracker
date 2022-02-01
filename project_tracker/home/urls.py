from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='home'),
    path('login/',views.logins,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign-up/',views.SignUp,name='sign-up'),
    path('remove_client/<int:id>/',views.remove_client,name='remove_client'),
    path('<int:id>/',views.update_client,name='update_client'),
]
