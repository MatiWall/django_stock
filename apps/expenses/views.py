from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse

from django.views.generic import TemplateView, UpdateView, View

from .models import Category, Expense, Income
from .forms import ExpenseForm, IncomeForm, AmountFilterForm, CategoryFilterForm, DateFilterForm
from .serializers import ExpenseSerializer, IncomeSerializer


from django.contrib import messages

from django.core.paginator import Paginator
from .pagination import customPagination


from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

import json
from datetime import datetime, timedelta



class home(TemplateView):
    template_name = 'expenses/home.html'

    def get(self, request):

        amountForm = AmountFilterForm()
        categoryForm = CategoryFilterForm(request = request)
        dateForm = DateFilterForm()
        
        return render(request, self.template_name, {'amountForm' : amountForm, 'categoryForm': categoryForm, 'dateForm' : dateForm})


class addExpense(TemplateView):
    template_name = 'expenses/addExpense.html'

    def get(self, request):
        
        form = ExpenseForm(request = request)
        context = {'form' : form}

        return render(request, self.template_name, context)


    def post(self, request):

        form = ExpenseForm(data = request.POST,request = request)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            #messages.success(request, 'Form submission successful')
            return redirect(reverse('expenses:expenses'))

        #messages.success(request, 'Form submission failed')
        return render(request, self.template_name, context)
        

class editExpense(TemplateView):
    template_name = 'expenses/editExpense.html'
 

    def get(self, request, pk):
        
        exp = Expense.objects.get(pk = pk)
       
        form = ExpenseForm(instance = exp, request = request)

        context = {'form' : form, 'expense' : exp}
        return render(request, self.template_name, context)


    def post(self, request, pk):
        
        exp = Expense.objects.get(pk = pk)
       
        form = ExpenseForm(data = request.POST, instance = exp, request = request)

        if form.is_valid():
            f = form.save(commit = False)
            f.user = request.user
            f.save()
            return redirect(reverse('expenses:expenses'))
        
        return redirect(reverse('expenses:edit-expense'))




def deleteExpense(request, pk):
    exp = Expense.objects.get(pk = pk)
    exp.delete()
    return redirect(reverse('expenses:expenses'))





def searchExpenses(request):

    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        
        exp = Expense.objects.filter(
            amount__istartswith = search_str, user = request.user) | expense.objects.filter(
            date__icontains = search_str, user = request.user) | expense.objects.filter(
            description__icontains = search_str, user = request.user) | expense.objects.filter(
            category__name__icontains = search_str, user = request.user) 

        data = exp.values()
        return JsonResponse(list(data), safe = False)


class searchExpensesListView(ListAPIView):
    serializer_class = ExpenseSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    sarch_fields = ['amount', 'date', 'description', 'category_name']
    pagination_class = customPagination


    def get_queryset(self):
        queryList = Expense.objects.filter(user = self.request.user)
        return queryList





class expensesSummary(TemplateView):
    template_name = 'expenses/expensesSummary.html'

    def get(self, request):
        return render(request, self.template_name, {})


   

def expensesCategorySummary(request):

    today = datetime.date(datetime.today())
    six_month_ago = today - timedelta(days = 30*6)
    expenses = Expense.objects.filter(user = request.user,
            date__gte = six_month_ago, date__lte = today
        )


    def get_catrgory(expense):
        return expense.category

    def get_expense_category_amount(expenses, category):
        amount = 0
        filtered_by_category = expenses.filter(category = category)

        for item in filtered_by_category:
            amount += item.amount
        return amount


    category_list = list(set(map(get_catrgory, expenses)))

    finalrep = {}
    for x in expenses:
        for y in category_list:
            finalrep[str(y)] = get_expense_category_amount(expenses, y)

    return JsonResponse(finalrep)
    






class incomeView(TemplateView):
    template_name = 'expenses/income/income.html'

    def get(self, request):
        income = Income.objects.all()
        return render(request, self.template_name, {'income': income})


class addIncomeView(TemplateView):
    template_name = 'expenses/income/addIncome.html'

    def get(self, request):
        form = IncomeForm(request = request)

        return render(request, self.template_name, {'form' : form})

    def post(self, request):

        form = IncomeForm(data = request.POST, request = request)

        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            #messages.success(request, 'Form submission successful')
            return redirect(reverse('expenses:income'))

        #messages.success(request, 'Form submission failed')
        return render(request, self.template_name, {})
        

class editIncomeView(TemplateView):
    template_name = 'expenses/income/addIncome.html'
 

    def get(self, request, pk):
        
        income = Income.objects.get(pk = pk)
       
        form = IncomeForm(instance = income, request = request)

        context = {'form' : form}
        return render(request, self.template_name, context)


    def post(self, request, pk):
        
        income = Income.objects.get(pk = pk)
       
        form = IncomeForm(data = request.POST, instance = income, request = request)

        if form.is_valid():
            f = form.save(commit = False)
            f.user = request.user
            f.save()
            return redirect(reverse('expenses:income'))
        
        return redirect(reverse('expenses:edit-income'))



class incomeListView(ListAPIView):
    serializer_class = IncomeSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    sarch_fields = ['amount', 'date', 'description', 'source_name']

    def get_queryset(self):
        return Expense.objects.filter(user = self.request.user)


def deleteIncomeView(request, pk):
    income = Income.objects.get(pk = pk)
    income.delete()
    return redirect(reverse('expenses:income'))

