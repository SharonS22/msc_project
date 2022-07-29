from django.http import JsonResponse
from django.shortcuts import render
from medplus.models import data

from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    # query database to list the latest 5 outbreaks
    highest = data.objects.order_by('-updates').values('outbreak').distinct()[:1]
    last_reported = data.objects.order_by('-id')[:5]
    new_outbreaks = data.objects.filter(updates=1)
    newly_emerged = new_outbreaks.order_by('date')[:5]
    outbreaks = data.objects.all()

    #Total no of outbreaks
    count = data.objects.count()

    #Total no of outbreaks per continent
    asia = data.objects.filter(continent__contains="Asia").count()
    asia = int(asia)
    africa = data.objects.filter(continent__contains="Africa").count()
    africa = int(africa)
    europe = data.objects.filter(continent__contains="Europe").count()
    europe = int(europe)
    north_america = data.objects.filter(continent__contains="North America").count()
    north_america = int(north_america)
    south_america = data.objects.filter(continent__contains="South America").count()
    south_america = int(south_america)
    oceania = data.objects.filter(continent__contains="Oceania").count()
    oceania = int(oceania)
    global_count = data.objects.filter(continent__contains="Global").count()
    global_count = int(global_count)

    labels = ['Asia', 'Africa', 'Europe', 'North America', 'Oceania', 'South America', 'Global']
    defaultData = [asia, africa, europe, north_america, oceania, south_america, global_count]

    #highest cases continent
    values = [defaultData]
    highest_case = values[0]
    for number in values:
        if number > highest_case:
            highest_case = number

    context_dict = {
    'last_reported' : last_reported,
    'newly_emerged' : newly_emerged,
    'highest_reported' : highest,
    'outbreak_data': outbreaks,
    'count' : count,
    'labels' : labels,
    'defaultData' : defaultData,
    'highest_case' : highest_case,
    }
    return render(request, 'medplus/index.html', context_dict)
