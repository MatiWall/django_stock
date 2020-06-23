from django import forms
from datetime import date, timedelta



class DateInput(forms.DateInput):
    input_type = 'date'



class historicalDataOptions(forms.Form):
    Ticker = forms.CharField(max_length = 10, label = 'Ticker')
    
    start_date = forms.DateField( widget = DateInput, input_formats = ('%d/%m/%Y',) , initial = date.today()-timedelta(days = 365))
    end_date = forms.DateField(widget = DateInput, initial = date.today() )

    chartType = forms.CharField(widget=forms.HiddenInput(), initial='Hist', max_length = 20) 





