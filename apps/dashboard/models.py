import django
from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
# Create your models here.



'''class Company(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    ticker = models.CharField(max_length = 10, unique = True)
    description = models.TextField(max_length = 200)
    addedDateTime = models.DateTimeField(default = django.utils.timezone.now)
   
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
'''

class dashboardGrid(models.Model):
    grid_layout = JSONField()
    name = models.CharField(max_length = 100, primary_key = True)








class dashboardComponentOptions(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name



#class historicalStockData(models.Model):
 #   name = models.ForeignKey('dashboardComponentOptions', on_delete = models.CASCADE)
  #  start_date = models.DateField()
   # end_date = models.DateField()
   # data = JSONField()

