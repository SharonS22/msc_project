from django.shortcuts import render
from medplus.models import data
from django.http import HttpResponse

def dashboard(request):
    # query database to list teh latest 5 outbreaks
    context_dict = {}
    #highest_reported = Data.objects.order_by('updates')[:5]
    #last_reported = data.objects.all()
    last_reported = data.objects.order_by('date')[:5]
   # new_outbreaks = Data.objects.filter(updates='01')
    #newly_emerged = new_outbreaks.order_by('date')[:5]
    #context_dict = {
    #'last_reported' : last_reported,
   # context_dict['last_reported'] = last_reported
    #context_dict['newly_emerged'] = newly_emerged
   # }
    return render(request, 'medplus/dashboard.html', {'last_reported' : last_reported})
   # return response

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