from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.

def searchResult(request):
    products=None
    query=None
    if 'g' in request.GET:
        query=request.GET.get('g')
        products=Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query':query,'products':products})



