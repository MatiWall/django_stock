from django.forms import ModelForm
from .models import accounts



class accountForm(ModelForm):
    class Meta:
        model = accounts 
        fields = ['name', 'account_type', 'cash_balance']
