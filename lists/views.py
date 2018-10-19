from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
#   Item.objects.first().delete()

    item_list = Item.objects.all()
    return render(request, 'home.html', {'items': item_list})

# Create your views here.
