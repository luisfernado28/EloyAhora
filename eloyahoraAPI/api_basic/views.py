from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

# Create your views here.

@csrf_exempt
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer= UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data= JSONParser().parse(request)
        serializer= UserSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)