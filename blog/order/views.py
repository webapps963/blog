from django.shortcuts import render

# Create your views here.
def order(request):
    '''
    Render the order page
    '''
    return render(request, 'order/order.html')