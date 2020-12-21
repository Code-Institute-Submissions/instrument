from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def all_products(request):
    """ A view to show the products, the search function and sorting function """
    #This imports all the products
    products = Product.objects.all()

    #This sets the context as the products that we are passing through the products template.
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
# Copied from the home views.py but it is important to add in the context as we will be passing items through.

def product_detail(request, product_id):
    """ A view to show the product detail. """
    #This imports all the products
    product = get_object_or_404(Product, pk=product_id)

    #This sets the context as the products that we are passing through the products template.
    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
# Copied from the home views.py but it is important to add in the context as we will be passing items through.