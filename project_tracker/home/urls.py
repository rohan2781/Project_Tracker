from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='home'),
    path('login/',views.logins,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('sign-up/',views.SignUp,name='sign-up'),
    path('remove_client/<int:id>/',views.remove_client,name='remove_client'),
    path('<int:id>/',views.update_client,name='update_client'),
    path('account/<str:id>',views.client,name='client'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
