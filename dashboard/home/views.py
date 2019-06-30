from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    dest1= User()
    return render(request,'index1.html',{'dest1':dest1})
    

