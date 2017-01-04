from django.shortcuts import render, redirect
from django.contrib import messages
from blog.settings import LOGIN_URL
# Create your views here.
def connection(request):
    '''
    Render the connection page
    '''
    return render(request, 'connection/connection.html')

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect('account:login')
        return func(request, *args, **kwargs)
    return auth