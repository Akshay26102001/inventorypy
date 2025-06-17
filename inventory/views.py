from django.shortcuts import render
from .models import Product

def dashboard(request):
    products = Product.objects.all()
    return render(request, 'inventory/dashboard.html', {'products': products})