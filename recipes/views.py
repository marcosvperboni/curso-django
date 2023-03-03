from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('home 2 ')

def contato(request):
    return HttpResponse('contao 2 ')

def sobre(request):
    return HttpResponse('sobre 2 ')


