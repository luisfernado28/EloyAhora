import kwargs as kwargs
from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.
from .models import *
def main_view(request):
    return render(request, 'pages/index.html ')


def users_view(request, pk):
    user= User.objects.all()

    context= {'user':user}
    return render(request, 'pages/users.html ',context)

def second_view(request):
    return render(request, 'pages/second.html ')

