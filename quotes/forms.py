from django import forms
from .models import stockTickers

class stockForm(forms.ModelForm):
    class Meta:
        model = stockTickers
        fields = ["ticker"]
