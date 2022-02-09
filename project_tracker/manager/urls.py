from django.contrib import admin
from django.urls import path
from manager import views
urlpatterns = [
    path('', views.manager,name='manager'),
    path('client/',views.admin_client,name='admin_client'),
    path('view_developers/',views.developer,name='view_developers'),
    path('remove_developer/<int:id>/',views.remove_developer,name='remove_developer'),
    path('<int:id>/',views.update_developer,name='update_developer'),
]
