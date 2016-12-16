from django.shortcuts import render

# Create your views here.
def connection(request):
    '''
    Render the connection page
    '''
    return render(request, 'connection/connection.html')