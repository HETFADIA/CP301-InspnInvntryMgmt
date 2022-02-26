from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
import random
from .models import Users
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.core import serializers

def RegisterView(request):
    if(request.user.is_authenticated):
        return redirect('HomeView')

    if request.method == 'POST':
        email = request.POST.get('email')
        dept=request.POST.get('dept')
        password1 = request.POST.get('password')
        isadmin = request.POST.get('isAdmin')

        if isadmin == "true":
            isadmin = 1

        if len(User.objects.filter(email=email)) == 0:
            hashed_pwd = make_password(password1)
            Users.objects.create(email = email, password = hashed_pwd, department=dept, isAdmin=isadmin)
            user = User.objects.create_user(username=email,password=password1)
            user.save()
            user = authenticate(username = email , password = password1)
            login(request, user)
            return redirect("HomeView")
        else:
            return render(request, 'users/register.html', {'code': 1, 'msg' : 'User already exists.'})
    return render(request, 'users/register.html', {'code': 0})
    
@login_required(login_url='login/')
def HomeView(request):
    return render(request, 'home/index.html')
    
def LoginView(request):
    if(request.user.is_authenticated):
        return render(request, 'home/index.html')
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if(email != "" and password != ""):
            user = authenticate(username = email, password = password)
            if(user != None):
                login(request, user)
                return redirect('HomeView')
            else:
                return render(request, 'users/login.html', {'code': '1', 'msg': 'Invalid Credentials.'})
        else:
            return render(request, 'users/login.html', {'code' : '1', 'msg': 'Fields cannot be empty.'})
    return render(request, 'users/login.html', {'code' : '0'})

@login_required(login_url = '')
def LogoutView(request):
    logout(request)
    return redirect('RegisterView')