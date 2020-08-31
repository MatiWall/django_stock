from django import forms 
from bootstrap_datepicker_plus import DateTimePickerInput


from .models import JournalAction 

class journalActionForm(forms.ModelForm):
    class Meta:
        model = JournalAction
        fields = ['action', 'action_reason', 'price', 'commision', 'fees']
