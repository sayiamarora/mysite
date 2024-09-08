from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def index(request):
    list_of_items=Item.objects.all()

    return HttpResponse(list_of_items)

def item(request):
    return HttpResponse("<h1>this is an selected item</h1>")