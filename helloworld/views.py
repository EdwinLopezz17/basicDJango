from django.http import HttpResponse


def greet(request):
    return HttpResponse("Hello developer")

def farewell(request):
    return HttpResponse("Good bye developer")

def adult(request, age):
    if age>=18:
        return HttpResponse("You're of age")
    
    return HttpResponse("You are not of age")

