from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, timedelta
from django.utils.timezone import now


# Create your models here.




class tradingStrategyChoices(models.Model):
    strategyChoice = models.CharField(max_length=25, primary_key = True, default = 'None')

    created = models.TimeField(auto_now_add = True)
    updated = models.TimeField(auto_now = True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.strategyChoice





class currenciesChoices(models.Model):
    currency = models.CharField(max_length = 4, primary_key = True, default = 'None')

    created = models.TimeField(auto_now_add = True)
    updated = models.TimeField(auto_now = True)

    user = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.currency



class journalEntry(models.Model):


    side_choices = (
        ('long', 'Long'),
        ('short', 'Short')
        )

    status_choices = (
        ('open', 'Open'),
        ('win', 'Win'),
        ('loss', 'Loss')
    )

     

    ticker = models.CharField(max_length = 10, blank= True, null = True)
    status = models.CharField(max_length = 10, choices = status_choices, default = 'open' )
    name = models.CharField(max_length = 40, blank= True, null = True)

    entry_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    exit_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    currency = models.CharField(max_length = 40, blank= True, null = True)

    size = models.IntegerField(blank= True, null = True)
    side = models.CharField(max_length = 40, choices = side_choices, default='long')


    strategy = models.CharField( max_length = 40, blank= True, null = True)
    
    position_opened = models.DateTimeField(default = now, blank= True)
    position_closed = models.DateTimeField(blank = True, null = True)

    found_via = models.CharField(max_length = 50, blank = True)
    reason_bought = models.TextField(blank = True, null = True)
    reason_sold = models.TextField(blank = True, null = True)
    notes = models.TextField(blank = True, null = True) 

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    user = models.ForeignKey(User,  on_delete=models.CASCADE)
