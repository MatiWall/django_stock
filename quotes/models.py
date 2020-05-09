import django
from django.db import models
from django.contrib.postgres.fields import JSONField
from datetime import datetime
# Create your models here.



class Company(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    ticker = models.CharField(max_length = 10, unique = True)
    description = models.TextField(max_length = 200)
    addedDateTime = models.DateTimeField(default = django.utils.timezone.now)
   
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class dashboardGrid(models.Model):
    id = models.DateTimeField(auto_now=True, primary_key=True)
    gridLayout = JSONField()
    name = models.CharField(max_length = 100, unique = True)

