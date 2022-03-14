from django.urls import path
from . import views

urlpatterns = [
    path('initiate/', views.CreateRequest, name = 'CreateRequest'),
    path('list/', views.RequestPending, name = 'RequestPending'),
]