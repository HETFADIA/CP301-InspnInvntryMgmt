from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core import serializers

def LoginView(request):
    return render(request, 'users/login.html')