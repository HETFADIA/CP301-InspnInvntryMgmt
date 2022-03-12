from django.urls import path
from . import views

urlpatterns = [
    path('newinvoice/', views.fill_Invoice, name = 'newInvoice'),
]