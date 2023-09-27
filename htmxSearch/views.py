from django.shortcuts import render
from .models import *
# Create your views here.

def product_search(request):
    query = request.GET.get('q', '')
    products = product.objects.filter(name__icontains=query)
    context = {
        'products': products, 
        'query': query
        }

    return render(request, 'htmxSearch/product_search.html', context)