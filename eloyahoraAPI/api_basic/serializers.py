from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','firstname','lastname','mail','typeofuser','cellphone','direction','contact']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # TODO read about how to serialize many to many relations

        # fields = ['id','nameofproduct','weight','dimentions','color','brand','owner','tags','description']
        fields= '__all__'





