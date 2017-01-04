from django.shortcuts import render, redirect, get_object_or_404 
from main.models import Main
from main.forms import MainForm
from django.contrib import messages
from connection.views import admin_required
import datetime

def main(request):
    '''
    Show "Hello world" in the main page
    '''
    mains = Main.objects.all()
    itemsList = []
    for main in mains:
        items = [main]
        itemsList.append(items)
    context = {'itemsList':itemsList}
    return render(request, 'main/main.html', context)

def about(request):
    '''
    Render the about page
    '''
    return render(request, 'main/about.html')

@admin_required
def mainCreate(request):
    '''
    Create a new article instance
        1. If method is GET, render an empty form
        2 . If method is POST, perform form validation. Display error messages if the form is invalid
        3. Save the form to the model and redirect to the article page
    '''
    template = 'main/mainCreateUpdate.html'
    if request.method == 'GET':
        print(MainForm())
        return render(request, template, {'mainForm':MainForm()})
    # POST
    mainForm = MainForm(request.POST)
    if not mainForm.is_valid():
        return render(request, template, {'mainForm':mainForm})
    mainForm.save()
    messages.success(request, '最新消息已新增')
    return redirect('main:main')


def mainRead(request, mainId):
    '''
    Read an article
        1. Get the "article" instance using "articleId"; redirect to the 404 page if not found
        2. Render the articleRead template with article instance and its
    associated comments
    '''
    mainToRead = get_object_or_404(Main, id=mainId)
    context = {
        'main': mainToRead,
    }
    return render(request, 'main/mainRead.html', context)

@admin_required
def mainUpdate(request, mainId):
    '''
    Update the article instance:
        1. Get the article to update; redirect to 404 if not found
        2. Render a bound form if the method is GET
        3. If the form is valid, save it to the model, otherwise render a
    bound form with error messages
    '''
    mainToUpdate = get_object_or_404(Main, id=mainId)
    template = 'main/mainCreateUpdate.html'
    if request.method == 'GET':
        mainForm = MainForm(instance=mainToUpdate)
        return render(request, template, {'mainForm':mainForm, 'main':mainToUpdate})
    # POST
    mainForm = MainForm(request.POST, instance=mainToUpdate)
    if not mainForm.is_valid():
        return render(request, template, {'mainForm':mainForm, 'main':mainToUpdate})
    mainForm.save()
    messages.success(request, '最新消息已修改')
    return redirect('main:mainRead', mainId=mainId)


















