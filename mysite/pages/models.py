
from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=200)
    cellphone = models.CharField(max_length=20)
    email= models.EmailField()
    lastname= models.CharField(max_length=200)

    def __str__(self):
        return self.firstname+"  "+self.lastname

class Tag(models.Model):
    name= models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Products(models.Model):
    STATUS = (
        ('Available','Disponible'),
        ('Out of stock', 'Fuera de Stock'),
    )
    owner= models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    tags= models.ManyToManyField(Tag)
    name= models.CharField(max_length=200)
    dimensions= models.CharField(max_length=150)
    brand=models.CharField(max_length=200)
    status = models.CharField(max_length=200,choices=STATUS)

    def __str__(self):
        return self.name

