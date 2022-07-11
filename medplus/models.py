from django.db import models


class Data(models.Model):
    outbreak = models.CharField(("outbreak"), max_length=100)
    full_loc = models.CharField(("full location"), max_length=100)
    place = models.CharField(("place"), max_length=50)
    continent= models.CharField(("continent"), max_length=100)
    updates = models.IntegerField(("number of updates"))
    date = models.DateField(("date"))
    
    