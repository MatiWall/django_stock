from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User




# Create your models here.


class portfolio(models.Model):

    name = models.CharField(max_length = 100)

    notes = models.TextField(blank = True, null = True) 

    selected = models.BooleanField(default = False)


    created = models.TimeField(auto_now_add = True)
    updated = models.TimeField(auto_now = True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




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



class journal(models.Model):

    type_choices = (
        ('share', 'Share'),
        ('crypto', 'Crypto'),
        ('forex', 'Forex'),
        ('futures', 'Futures')
    )

    portfolio = models.ForeignKey(portfolio, on_delete = models.CASCADE)

    market = models.CharField(max_length = 20, choices = type_choices, default = 'share')

    ticker = models.CharField(max_length = 10, blank= True, null = True)
    name = models.CharField(max_length = 40, blank= True, null = True)

    currency = models.CharField(max_length = 40, blank= True, null = True)

    strategy = models.CharField( max_length = 40, blank= True, null = True)
      
    found_via = models.CharField(max_length = 50, blank = True)
    
    notes = models.TextField(blank = True, null = True) 

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    user = models.ForeignKey(User, on_delete = models.CASCADE)


class journalAction(models.Model):

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

    journal_entry = models.ForeignKey(journal, on_delete = models.CASCADE) 


    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    

class journalTargets(models.Model):

    target_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    journal = models.ForeignKey(journal, on_delete = models.CASCADE) 

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


class journalStopLosses(models.Model):

    stop_loss = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    journal = models.ForeignKey(journal, on_delete = models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    

class journalScreenShots(models.Model):

    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images')
    journal = models.ForeignKey(journal, on_delete = models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title