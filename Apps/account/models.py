from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model): # model profile
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True) 
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='profile/', null=True, blank=True)  
    
    def __str__(self):
        return f'{self.user_id.username} Profile'