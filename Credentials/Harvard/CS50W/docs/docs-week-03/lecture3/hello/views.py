from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world!")
    rturn render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

#now let's crete a placeholder for templates
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")