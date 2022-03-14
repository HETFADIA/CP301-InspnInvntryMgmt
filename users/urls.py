from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name = 'LoginView'),
    path('changePassword/', views.ChangePasswordView, name = 'ChangePasswordView'),
    path('logout/', views.LogoutView, name = 'LogoutView'),
    path('register/', views.RegisterView, name = 'RegisterView'),
]