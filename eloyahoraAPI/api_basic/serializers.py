from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):

    firstname = serializers.CharField(max_length=200)
    lastname = serializers.CharField(max_length=200)
    mail = serializers.EmailField()
    typeofuser = serializers.IntegerField( )
    cellphone = serializers.CharField(max_length=15)
    direction = serializers.CharField(max_length=300)
    contact = serializers.CharField(max_length=300)

    def create(self, validated_data):

        return User.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.firstname = validated_data.get('firstname',instance.firstname)
        instance.lastname = validated_data.get('lastname',instance.lastname)
        instance.mail = validated_data.get('mail',instance.mail)
        instance.typeofuser = validated_data.get('typeofuser',instance.typeofuser)
        instance.cellphone =validated_data.get('cellphone',instance.cellphone)
        instance.direction = validated_data.get('direction',instance.direction)
        instance.contact = validated_data.get('contact',instance.contact)
        instance.save()
        return instance





