from django.db import models
from django.contrib.auth.models import User

from datetime import datetime, timedelta
from django.utils.timezone import now


# Create your models here.


class portfolio(models.Model):

    name = models.CharField(max_length = 100)


    created = models.TimeField(auto_now_add = True)
    updated = models.TimeField(auto_now = True)





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

    type_choices = (
        ('share', 'Share'),
        ('crypto', 'Crypto'),
        ('forex', 'Forex'),
        ('futures', 'Futures')
    )

    portfolio = models.ForeignKey(portfolio, on_delete = models.CASCADE)

    market = models.CharField(max_length = 20, choices = type_choices)

    ticker = models.CharField(max_length = 10, blank= True, null = True)
    name = models.CharField(max_length = 40, blank= True, null = True)

    currency = models.CharField(max_length = 40, blank= True, null = True)

    strategy = models.CharField( max_length = 40, blank= True, null = True)
      
    found_via = models.CharField(max_length = 50, blank = True)
    
    notes = models.TextField(blank = True, null = True) 

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    user = models.ForeignKey(User,  on_delete=models.CASCADE)



class journalEntryAction(models.Model):

    action_choices = (
        ('buy', 'Buy'),
        ('sell', 'Sell')
    )

  

    action = models.CharField(max_length = 10, choices = action_choices)
   

    reason_bought = models.TextField(blank = True, null = True)
    reason_sold = models.TextField(blank = True, null = True)
    
    entry_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    exit_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)


    commision = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    fees = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)

    journal_entry = models.ForeignKey(journalEntry, on_delete = models.CASCADE) 

    

class journalEntryTargets(models.Model):

    target_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    journalEntry = models.ForeignKey(journalEntry, on_delete = models.CASCADE) 


class journalEntryStopLosses(models.Model):

    stop_loss = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    journalEntry = models.ForeignKey(journalEntry, on_delete = models.CASCADE)
    

class journalEntryScreenShots(models.Model):

    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images')
    journalEntry = models.ForeignKey(journalEntry, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
