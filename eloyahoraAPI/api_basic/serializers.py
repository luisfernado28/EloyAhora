from rest_framework import serializers
from .models import *

class userSerializer(serializers.Serializer):
    typeuser = (
        (1, 'Vendedor'),
        (2, 'Comprador'),
    )
    firstname = serializers.CharField(max_length=200, null=False)
    lastname = serializers.CharField(max_length=200, null=False)
    mail = serializers.EmailField(null=False)
    typeofuser = serializers.IntegerField(choices=typeuser, null=False)
    cellphone = serializers.CharField(max_length=15, null=False)
    direction = serializers.CharField(max_length=300)
    contact = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return User.objects.create(validated_data)

