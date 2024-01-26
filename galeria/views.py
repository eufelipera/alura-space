from django.shortcuts import render

#criando funcao principal da aplicação
def index(request):
    return render(request, 'index.html')
