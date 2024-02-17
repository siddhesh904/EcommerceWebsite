from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from accounts.models import *
# Create your views here.

def register_user(request):
    # **** VERY IMPORTANT (POST) always write Capital Letter.
    if (request.method == "POST"):
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if (user.exists()):
            messages.info(request, "Username alredey exists!")
            return redirect('accounts/register')

        queryset = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        queryset.set_password(password)
        queryset.save()
        messages.info(request, "Account created successfully")
        return redirect('/')
    return render(request, 'register.html')


def login_user(request):
    if (request.method == 'POST'):
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username)
        if (not user.exists()):
            messages.error(request, 'Invalid Username')
            return redirect('accounts/login')
        userAuth = authenticate(username=username, password=password)
        if (userAuth is None):
            messages.error(request, 'Invalid Password')
            return redirect('accounts/login')
        else:
            login(request, userAuth)
            return redirect('/')

    return render(request, 'login.html')



def logout_user(request):
    logout(request)
    return redirect('login')





    


    
