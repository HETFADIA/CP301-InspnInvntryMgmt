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
from django.core.mail import send_mail
f=open("debug.txt","w")
f.write("hi")
def _send_email(subject,msg,_from,to):
    print(subject,msg,_from,to)
    send_mail(
        subject,
        msg,
        _from,
        [to],
        fail_silently=False,
    )
def RegisterView(request):
    print(request.user)
    if(request.user.is_authenticated):
        return redirect('HomeView')

    if request.method == 'POST':
        email = request.POST.get('email')
        dept=request.POST.get('dept')
        password1 = request.POST.get('password')
        isadmin = request.POST.get('isAdmin')
        if isadmin == "true":
            isadmin = 1
        else:
            isadmin=0
        print("b",User.objects.filter(email=email).exists(),User.objects.filter(email=email).exists()==False)
        print(User.objects.filter(username=email))
        if User.objects.filter(username=email).exists():
            f.write("user already exists")
        if len(User.objects.filter(username=email))==0:
            hashed_pwd = make_password(password1)
            Users.objects.create(email = email, password = hashed_pwd, department=dept, isAdmin=isadmin)
            user = User.objects.create_user(username=email,password=password1)
            user.save()
            
            user = authenticate(username = email , password = password1)
            login(request, user)
            return redirect("HomeView")
        else:
            f.write("user already exists na")
            
            user = authenticate(username = email , password = password1)
            if user!=None:
                login(request, user)
                return redirect("HomeView")
            else:
                return render(request, 'users/register.html', {'code': 1, 'msg' : 'Wrong creditentials.'})
            return render(request, 'users/register.html', {'code': 1, 'msg' : 'User already exists.'})
    return render(request, 'users/register.html', {'code': 0})
    
@login_required(login_url='login/')
def HomeView(request):
    return render(request, 'home/index.html')
    
def LoginView(request):
    print(request.user)
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


def PasswordResetView(request):
    return render(request, 'home/index.html')