from django.contrib import messages
from django.shortcuts import render, redirect

from order.forms import OrderForm
from order.models import Order


# Create your views here.
def order(request):
    '''
    Render the order page
    '''
    return render(request, 'order/order.html')

def orderCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2 . If method is POST, perform form validation. Display error messages if the form is invalid
        3. Save the form to the model and redirect to the article page
    '''
    template = 'order/orderCreate.html'
    if request.method == 'GET':
        print(OrderForm())
        return render(request, template, {'orderForm':OrderForm()})
    # POST
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':orderForm})
    orderForm.save()
    messages.success(request, '文章已新增')
    return redirect('order:order')