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
        fields= '__all__'





