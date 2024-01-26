from django.shortcuts import render
from django.http import HttpResponse

#criando funcao principal da aplicação
def index(request):
    return HttpResponse('<h1>Hello World</h1>')
