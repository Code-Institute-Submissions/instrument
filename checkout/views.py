
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51I9YB5E9u9fEGOsf6STzF6iPgmQrUWW6JGEchobeySk7EM4vZQ8bNZXkTk6GI3Fqhicl5p0SQKTK4SudeGgNtrOS006THLXVTx',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)