from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    dest1= User()
    return render(request,'index.html',{'dest1':dest1})
    

def login(request):
    return render(request,'login.html')