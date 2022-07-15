from django.db import models

class data(models.Model):
    id = models.IntegerField(default=1, unique=True, primary_key=True)
    outbreak = models.CharField(max_length=100)
    full_loc = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    continent= models.CharField(max_length=100)
    updates = models.IntegerField()
    date = models.DateField()

    class Meta:
        verbose_name_plural = 'datas'
        #db_table = 'medplus_data'
       # managed = False
    
    def __str__(self):
        return self.outbreak
    
    