from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from rest_framework.authentication import   TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#Generic API views
class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

class ProductViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Class Based API views (Unused)
class ProductAPIView(APIView):

    def get(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class Based API views (Unused)
class ProductDetails(APIView):

    def get_product(self, id):
        try:
            return  User.objects.get(pk=id)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self,request,id):
        product= self.get_product(id)
        serializer = UserSerializer(product)
        return Response(serializer.data)

    def put(self,request,id):
        product = self.get_product(id)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        product = self.get_product(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Function Based API views
@api_view(['GET','POST'])
def user_list(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer= UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer= UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail(request,pk):
    try:
        user= User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer= UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
