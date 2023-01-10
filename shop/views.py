from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Product

# Create your views here.
def product_list(request):
    return render(request, 'shop/mainpage.html', {})
    
def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'shop/mainpage.html', {'products': products})

def index(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"mainpage.html", context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/productpage.html', {'product': product})