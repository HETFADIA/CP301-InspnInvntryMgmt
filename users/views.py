from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Departments
    
def RegisterView(request):

    if(request.user.is_authenticated):
        return redirect('HomeView')

    if request.method == 'POST':

        email = request.POST.get('email')
        dept=request.POST.get('dept')
        password = request.POST.get('password')
        print(dept)
        if len(User.objects.filter(username=email))==0:
            try:

                user = User.objects.create_user(username=email,password=password)
                user.save()
                Departments.objects.create(user = user, email = email, department=dept)

                user = authenticate(username = email , password = password)
                login(request, user)
                return redirect("HomeView")

            except Exception as e:

                print(e)
                return render(request, 'users/register.html', {'code': 1, 'msg' : 'Provide valid input values.'})
        else:

            return render(request, 'users/register.html', {'code': 1, 'msg' : 'User already exists.'})

    return render(request, 'users/register.html', {'code': 0})
    
def LoginView(request):

    if(request.user.is_authenticated):
        return redirect('HomeView')

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

def ChangePasswordView(request):

    if request.method == "POST":

        email = request.POST.get('email')
        old_password = request.POST.get('password')
        new_password=request.POST.get('new_password')
        new_password_repeat=request.POST.get('new_password_repeat')

        if(email != "" and old_password != ""):
            if new_password!=new_password_repeat:

                return render(request, 'users/changePassword.html', {'code': '1', 'msg': 'Confirm new password correctly'})

            if new_password==old_password:

                return render(request, 'users/changePassword.html', {'code': '1', 'msg': 'New password cannot be same as old password'})

            user = authenticate(username = email, password = old_password)

            if(user != None):

                t=User.objects.get(username=email)
                t.set_password(new_password)
                t.save()
                
                return render(request, 'users/login.html', {'code': '1', 'msg': 'Password Changed Successfull.'})
                
            else:
                return render(request, 'users/changePassword.html', {'code': '1', 'msg': 'Incorrect password.'})
        else:
            return render(request, 'users/changePassword.html', {'code' : '1', 'msg': 'Fields cannot be empty.'})

    return render(request, 'users/changePassword.html', {'code' : '0'})


@login_required(login_url = '/accounts/login/')
def LogoutView(request):
    
    logout(request)
    return redirect('RegisterView')