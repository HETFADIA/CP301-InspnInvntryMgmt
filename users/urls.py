from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name = 'LoginView'),
    path('logout/', views.LogoutView, name = 'LogoutView'),
    path('register/', views.RegisterView, name = 'RegisterView'),
    path('passwordreset/',views.PasswordResetView, name = 'PasswordResetView'),
    path('', views.HomeView, name = 'HomeView'),
]