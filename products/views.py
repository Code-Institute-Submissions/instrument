

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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