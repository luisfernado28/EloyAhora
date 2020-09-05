import kwargs as kwargs
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")


def settings(*args, **kwargs):
    return HttpResponse("<h1>Settings Pibe</h1>")
