from django.shortcuts import render
from django.utils import timezone
from .models import Product

# Create your views here.
def product_list(request):
    return render(request, 'shop/mainpage.html', {})
    
def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'shop/mainpage.html', {'products': products})
