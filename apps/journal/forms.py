from django import forms 
from bootstrap_datepicker_plus import DateTimePickerInput

from .models import tradingStrategyChoices, currenciesChoices, journalEntry


class tradingStrategyChoicesForm(forms.ModelForm):
    class Meta:
        model = tradingStrategyChoices
        fields = ['strategyChoice', 'user']

  




class journalEntryForm(forms.ModelForm):

    strategy = forms.ModelChoiceField(queryset=tradingStrategyChoices.objects.all())
    currency = forms.ModelChoiceField(queryset=currenciesChoices.objects.all())



    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(journalEntryForm, self).__init__(*args, **kwargs)

        self.fields['strategy'].queryset = tradingStrategyChoices.objects.filter(user=self.user)
        self.fields['currency'].queryset = currenciesChoices.objects.filter(user=self.user)

   
    

    class Meta:
        model = journalEntry
        exclude = ['user', 'created', 'updated']

        widgets = {
       
            'position_opened': DateTimePickerInput(),
            'position_closed': DateTimePickerInput(),
          
        }


 

    