from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/lists/the-only-list-in-the-world/')
#   Item.objects.first().delete()

    item_list = Item.objects.all()
    return render(request, 'home.html', {'items': item_list})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

# Create your views here.
