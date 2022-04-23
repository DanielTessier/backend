# ~/projects/django-web-app/merchex/listings/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from rest_framework import generics

from .serializers import PageConnection, CodePython
from .models import Connection

from .forms import RegistrationForm

def page_daccueil(request):
    context_dict = {'form': None}
    form = RegistrationForm()
    
    if request.method == 'GET':
            context_dict['form'] = form
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
            messages.success(request, 'Your data has been submitted')
        else:
            messages.error(request, 'Something is wrong in form.')
    
    return render(request, 'index.html', context_dict)

def page_carte_monde(request):
    return render(request, 'listings/page_carte_monde.html')

def page_niveau(request):
    text = ""
    form = CodePython(request.POST or None)
    
    if form.is_valid():
        text = form.cleaned_data['code']
        
    print(request.POST)
    
    return render(request, 
                'listings/page_niveau.html',
                {'form': form, 'element':text})
    
class Connection_view(generics.CreateAPIView):
    queryset = Connection.objects.all()
    serializer_class = PageConnection
    
def csrf_failure(request, reason=""):
    context_dict = {'form': None}
    form = RegistrationForm()
    cleaned_data = '0'
    print('///////////////////////////////////////////////////////////////////////////')
    print(request.method)
    print('///////////////////////////////////////////////////////////////////////////')
    if request.method == 'GET':
            context_dict['form'] = form
    elif request.method == 'POST':
        form = RegistrationForm(request.POST)
        context_dict['form'] = form
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)
    return render(request, 'listings/page_niveau.html', {'form': cleaned_data, 'element':cleaned_data})

def about(request):
    return HttpResponse('<h1>Créer par :</h1> <p>Daniel, Romain, Cedric et Adam <br /> Dans le cadre du trophée NSI</p>')