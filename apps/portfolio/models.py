from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class accounts(models.Model):
    ACCOUNT_TYPES = (('TRADITIONAL', 'Traditional IRA or 401(k)'),
                    ('ROTH', 'Roth IRA or 401(k)'),
                    ('Standard', 'Standard Brokerage'))

    name = models.CharField(max_length = 100)
    account_type = models.CharField(max_length = 100, choices = ACCOUNT_TYPES)
    cash_balance = models.FloatField(default = 0.0)
    user = models.ForeignKey(User, related_name = 'broker_account', null = True,  on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name



class positions(models.Model):

    name = models.CharField(max_length = 100)
    symbol = models.CharField(max_length = 10)
    shares = models.IntegerField()
    cost_basis = models.FloatField(default = 0.0)
    account = models.ForeignKey(accounts, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.symbol