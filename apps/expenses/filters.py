from django_filters import rest_framework as filters
from django import forms
from .models import Expense, Category
from django.db import models


class ExpenseFilter(filters.FilterSet):

    CHOICES = (
        ('date', 'Ascending date'),
        ('-date', 'Descending date'),
        ('amount', 'Ascending amount'),
        ('-amount', 'Descending amount'),

    )



    min_amount = filters.NumberFilter(label= 'Min amount',field_name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(label = 'Max amount', field_name="amount", lookup_expr='lte')

    start_date = filters.DateFilter(label = 'Start date',field_name = 'date', lookup_expr = 'gte',  widget=forms.TextInput(attrs={'type': 'date'}))
    end_date = filters.DateFilter(label = 'End date', field_name = 'date', lookup_expr = 'lte', widget=forms.TextInput(attrs={'type': 'date'}))

    category = filters.ModelMultipleChoiceFilter(field_name = 'category', queryset = Category.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={"checked":""}))

    ordering = filters.OrderingFilter(label = 'Ordering', choices = CHOICES, method = 'filter_by_order')

    description = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Expense
        fields = ['description', 'category', 'min_amount', 'max_amount']
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        request = kwargs['request']     
        self.filters['category'].queryset = Category.objects.filter(user=request.user)


    def filter_by_order(self, queryset, name, value):
        return queryset.order_by(*value)
    
 