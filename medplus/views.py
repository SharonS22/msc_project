from django.shortcuts import render

from django.http import HttpResponse
def dashboard(request):
    context_dict = {'boldmessage': 'hi'}
    return render(request, 'medplus/dashboard.html', context=context_dict)

def about(request):
    return HttpResponse("Welcome to about!")

def search(request):
    return HttpResponse("Welcome to search")

def data(request):
    return HttpResponse("Welcome to data")

def map(request):
    return HttpResponse("map")

def subscribe(request):
    return HttpResponse("Welcome medplus!")