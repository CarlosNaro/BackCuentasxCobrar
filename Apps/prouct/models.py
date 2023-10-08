from django.db import models

# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/', null=True, blank=True)