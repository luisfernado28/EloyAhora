import kwargs as kwargs
from django.http import HttpResponse, request
from django.shortcuts import render


# Create your views here.
def main_view(request):
    return render(request, 'pages/index.html ')

def second_view(request):
    return render(request, 'pages/second.html ')

