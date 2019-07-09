from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1=request.POST['password1']
        
        email=request.POST['email']
        phone_number=request.POST['phone_number']

        user=User.objects.create_user(username=username,first_name=first_name,email=email,password=password1,last_name=last_name,phone_number=phone_number)
        user.save()
        print('user created')
        return redirect("/")
    else:
        return render(request,'register.html')

def login(request):

    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("accounts/dashboard_.html")


    else:
        return render(request,'login.html')