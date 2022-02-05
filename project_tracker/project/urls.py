from django.contrib import admin
from django.urls import path
from project import views
urlpatterns = [
    path('', views.project,name='project'),
    path('new_project/', views.newProject, name='new_project'),
    path('projects/', views.projects, name='projects'),
    path('remove_project/<int:id>/',views.remove_project,name='remove_project'),
    path('<int:id>/',views.update_project,name='update_project'),
]
