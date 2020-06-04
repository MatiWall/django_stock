from django.forms import ModelForm
from django import forms
from .models import accounts, positions



class accountForm(ModelForm):
    class Meta:
        model = accounts 
        fields = ['name', 'account_type', 'cash_balance']


class positionForm(ModelForm):
    class Meta:
        model = positions
        fields = ['name', 'symbol', 'shares', 'cost_basis', 'account']

        widgets = {
            'text': forms.TextInput(attrs={
                'id': 'post-positions', 
                'required': True, 
            })
        }

  