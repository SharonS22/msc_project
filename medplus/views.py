from django.shortcuts import render
from medplus.models import data

def index(request):
    # query database to list the latest 5 outbreaks
    highest = data.objects.order_by('-updates').values('outbreak').distinct()[:1]
    last_reported = data.objects.order_by('-id')[:5]
    new_outbreaks = data.objects.filter(updates=1)
    newly_emerged = new_outbreaks.order_by('date')[:5]
    outbreaks = data.objects.all()

    #Total no of outbreaks
    count = data.objects.count()

    #Total number of outbreak per continent
    asia = data.objects.filter(continent="Asia").count() 
    africa = data.objects.filter(continent="Africa").count() 
    europe = data.objects.filter(continent="Europe").count() 
    north_america = data.objects.filter(continent="North America").count() 
    south_america = data.objects.filter(continent="South America").count() 
    oceania = data.objects.filter(continent="oceania").count() 

    context_dict = {
    'last_reported' : last_reported,
    'newly_emerged' : newly_emerged,
    'highest_reported' : highest,
    'outbreak_data': outbreaks,
    'count' : count,
    'asia' : asia,
    'africa' : africa,
    'europe' : europe,
    'north_america' : north_america,
    'south_america' : south_america,
    'oceania' : oceania,
    }
    return render(request, 'medplus/index.html', context_dict)
   # return response
