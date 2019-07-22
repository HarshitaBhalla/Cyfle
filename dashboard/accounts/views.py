from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'register.html')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password1,last_name=last_name)
                user.save()
                messages.info(request,'User Created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching!')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'dashboard_.html')
        else:
            messages.info(request,'Invalid Password or UserName')
            return redirect('login')
    else:
        return render(request,'login.html')