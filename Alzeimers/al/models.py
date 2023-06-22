from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
User=get_user_model()
class User(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10)
   
    email = models.EmailField(max_length=50, null='True')
    gender = models.CharField( max_length=1, blank=True, null=True)
    def __str__(self):
        return self.phone


# Create your models here.

