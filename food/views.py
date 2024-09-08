from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World of Django Here's my first Http Request")

def item(request):
    return HttpResponse("<h1>this is an selected item</h1>")