from rest_framework import serializers

from .models import Expense, Category




class ExpenseSerializer(serializers.ModelSerializer):
    category_name= serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'description','category_name']




class IncomeSerializer(serializers.ModelSerializer):
    source_name= serializers.ReadOnlyField(source='source.name')
    class Meta:
        model = Expense
        fields = ['id', 'amount', 'date', 'description','source_name']



class UserInputGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = None