from django import forms
from apps.journal.models import portfolio, Journal, JournalAction, JournalTargets





class JournalActionForm(forms.ModelForm):
    class Meta:
        model = JournalAction
        fields = ['action', 'action_reason', 'price', 'commision', 'fees']
      

class JournalTargetForm(forms.ModelForm):
    class Meta:
        model = JournalTargets
        fields = ['shares', 'target_price', 'stop_loss']