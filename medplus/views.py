from django.shortcuts import render
from medplus.models import data

def index(request):
    # query database to list the latest 5 outbreaks
    highest = data.objects.order_by('-updates').values('outbreak').distinct()[:1]
    last_reported = data.objects.order_by('-id')[:5]
    new_outbreaks = data.objects.filter(updates=1)
    newly_emerged = new_outbreaks.order_by('date')[:5]
    context_dict = {
    'last_reported' : last_reported,
    'newly_emerged' : newly_emerged,
    'highest_reported' : highest,
    }
    return render(request, 'medplus/index.html', context_dict)
   # return response
