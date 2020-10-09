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



class Journal(models.Model):

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

 



class JournalAction(models.Model):

    action_choices = (
        ('buy', 'Buy'),
        ('sell', 'Sell')
    )

  

    action = models.CharField(max_length = 10, choices = action_choices)
   

    action_reason = models.TextField(blank = True, null = True)
   
    price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)

    commision = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    fees = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)

    journal = models.ForeignKey(Journal, on_delete = models.CASCADE) 


    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    

class JournalTargets(models.Model):
    shares = models.IntegerField(default = 0)
    target_price = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)

    stop_loss = models.DecimalField(max_digits = 7, decimal_places = 2, blank= True, null = True)
    journal = models.ForeignKey(Journal, on_delete = models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    

class journalScreenShots(models.Model):

    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images', null = True, blank = True)
    notes = models.TextField(null=True, blank = True)
    journal = models.ForeignKey(Journal, on_delete = models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title