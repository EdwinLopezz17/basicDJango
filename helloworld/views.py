from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def greet(request):
    return HttpResponse("Hello developer")

def farewell(request):
    return HttpResponse("Good bye developer")

def adult(request, age):
    if age>=18:
        return HttpResponse("You're of age")
    
    return HttpResponse("You are not of age")

def dinamic(request, name):
    categories = ['code', 'design', 'marketing', 'sales']
    context = {'name': name, 'categories':categories}
    return render(request, 'dinamic.html', context)


def statics(request):
    return render(request, 'statics.html', {})

def herencia(request):
    return render(request, 'herencia.html', {})

def example(request):
    return render(request, 'example.html',{})

def other(request):
    return render(request, 'other.html',{})




