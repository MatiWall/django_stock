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



    



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['user']
