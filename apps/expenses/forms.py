from django import forms
from .models import Expense, Category, Income, IncomeSource

import datetime



class DateTimeInput(forms.DateTimeField):
    input_type = 'date'



class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        exclude = ['user']
        widgets = {
        'date': forms.TextInput(attrs={'type': 'date'}),
    }
        


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'





class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        exclude = ['user']
        widgets = {
        'date': forms.TextInput(attrs={'type': 'date'}),
    }
        


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
        self.fields['source'].queryset = IncomeSource.objects.filter(user=self.request.user)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



    
class AmountFilterForm(forms.Form):
    minimum = forms.FloatField()
    maximum = forms.FloatField()


    def __init__(self, *args, **kwargs):
        super(AmountFilterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class CategoryFilterForm(forms.Form):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CategoryFilterForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=self.request.user)
   


class DateFilterForm(forms.Form):

    start_date = forms.DateField(initial=datetime.date.today()-datetime.timedelta(days = 6*30), widget = forms.TextInput(attrs={'type': 'date'}) )
    end_date = forms.DateField(initial=datetime.date.today(), widget = forms.TextInput(attrs={'type': 'date'}) )
