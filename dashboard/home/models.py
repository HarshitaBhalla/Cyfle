from django.db import models

# Create your models here.

class User(models.Model):
    username= models.TextField()
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    password= models.TextField(max_length=20)
    email= models.CharField(max_length=30)
    number=models.TextField
