from django.db import models

# Create your models here.

class User(models.Model):
    typeuser = (
        (1, 'Vendedor'),
        (2, 'Comprador'),
    )
    firstname= models.CharField(max_length=200, null=False)
    lastname = models.CharField(max_length=200, null=False)
    mail     = models.EmailField(null=False)
    typeofuser= models.IntegerField(choices=typeuser, null=False)
    cellphone= models.CharField(max_length=15, null=False)
    direction = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)

    def __str__(self):
        return self.firstname + " "+ self.lastname

class Tag(models.Model):
    name= models.CharField(max_length=250,null=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    nameofproduct= models.CharField(max_length=200,null=False)
    weight=  models.CharField(max_length=200,null=False)
    dimentions= models.CharField(max_length=200,null=False)
    color= models.CharField(max_length=200,null=False)
    brand= models.CharField(max_length=200,null=False)
    owner= models.ManyToManyField(User)
    tags= models.ManyToManyField(Tag)
    description = models.TextField

    def __str__(self):
        return self.nameofproduct