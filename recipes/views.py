from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html', {
        'name': 'Marcos Perboni'
    })

def contato(request):
    return HttpResponse('contao 2 ')

def sobre(request):
    return HttpResponse('sobre 2 ')


