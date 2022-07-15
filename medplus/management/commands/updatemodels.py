from django.core.management.base import BaseCommand
import pandas as pd
from medplus.models import data
class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        #db connections
        df=pd.read_csv("promed_data1.csv")
        for ID,OUTBREAK,FULL_LOC,PLACE,CONTINENT,UPDATES,DATE in zip(df.id,df.outbreak,df.full_loc,df.place,df.continent,df.updates,df.date):
            models=data(id=ID,outbreak=OUTBREAK,full_loc=FULL_LOC,place=PLACE,continent=CONTINENT,updates=UPDATES,date=DATE)
            models.save()