from django.db import models


# Create your models here.
class User(models.Model):
    name = models.TextField()
    cellphone = models.TextField()
    email= models.EmailField()
    lastname= models.CharField(max_length=200)
