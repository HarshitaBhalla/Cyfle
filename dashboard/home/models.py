from django.db import models

# Create your models here.

class User(models.Model):
    username= models.TextField()
    name= models.CharField(max_length=20)
    img= models.ImageField(upload_to='pics')
    jobsa= models.TextField()

    
