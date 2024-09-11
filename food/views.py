from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.

def index(request):
    list_of_items=Item.objects.all()
    template=loader.get_template('food/index.html')
    context={
        'list_of_items':list_of_items,
    }
    return HttpResponse(template.render(context,request))

def item(request):
    return HttpResponse("<h1>this is an selected item</h1>")


def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request, 'food/detail.html',context)
