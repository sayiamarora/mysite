from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def index(request):
    list_of_items = Item.objects.all()
    context = {
        'list_of_items': list_of_items,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("<h1>This is a selected item</h1>")

def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, "food/item-forms.html", {"form": form})

def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-forms.html', {'form': form, 'item': item})


def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method=="POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item-delete.html',{'item':item})    
