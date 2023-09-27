from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField( upload_to='user/', null=True, blank=True)
# default='userDefault.png' ,

#tutorial de extender datos al usuario de django 
# https://www.youtube.com/watch?v=x0f4guW1zuA&ab_channel=C%C3%B3digoparaPrincipiantes