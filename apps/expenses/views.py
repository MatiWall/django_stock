from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import JsonResponse



from django.views.generic import TemplateView, UpdateView, View, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


from .models import Category, Expense, Income, IncomeSource
from .forms import ExpenseForm, IncomeForm
from .serializers import ExpenseSerializer, IncomeSerializer, UserInputGeneralSerializer


from django.contrib import messages

from django.core.paginator import Paginator
from .pagination import customPagination


from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

import json
from datetime import datetime, timedelta

from .filters import ExpenseFilter


class home(TemplateView):
    template_name = 'expenses/home.html'

    def get(self, request):

        categories = Category.objects.filter(user = request.user)
        expenseFilter = ExpenseFilter(request = request)
        return render(request, self.template_name, {'categories' : categories, 'filter': expenseFilter})


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







class searchExpensesListView(ListAPIView):
    serializer_class = ExpenseSerializer
    filter_class = ExpenseFilter
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







# General views

from .forms import CategoryForm
from django.forms import modelform_factory
from django.apps import apps

class generalView(TemplateView):
    template_name = 'expenses/general.html'


    def get(self, request):

        models = ['Category', 'IncomeSource']
       
        return render(request, self.template_name, {'models' : models})
   


class userdefinedInputView(CreateView):
    template_name = 'expenses/userdefinedInput.html'
    fields = ['name']

    def get(self, request, *args, **kwargs):
        self.object = None
        self.model_name = kwargs['model']
        context = super().get_context_data(**kwargs)
        context["object_list"] = self.model.objects.filter(user = self.request.user)
        context["model_name"] = self.model_name
        form_class = self.get_form_class()
        context['form'] = self.get_form(self.form_class)

        return self.render_to_response(context)


    def form_valid(self, form):
        f = form.save(commit = False)
        f.user = self.request.user
        f.save()
        return redirect(reverse('expenses:expenses'))

 
    def get_form_class(self):
        self.model = apps.get_model(app_label='expenses', model_name = self.model_name)
        return modelform_factory(self.model, fields=self.fields)




class userdefiendInputControlView(viewsets.ViewSet):
    

    def dispatch(self, request, *args, **kwargs):
        
        if (request.GET.get('model', None)):
            model_name = request.GET.get('model', None)
        elif( json.loads(request.body)['model']):
            model_name = json.loads(request.body)['model']


        
        self.model = apps.get_model(app_label='expenses', model_name = model_name)
        UserInputGeneralSerializer.Meta.model = self.model
        UserInputGeneralSerializer.Meta.exclude = ['user']

        self.serializer =  UserInputGeneralSerializer
        return super(userdefiendInputControlView, self).dispatch(request, *args, **kwargs)



    def list(self, request):
        
        queryset = self.model.objects.filter(user = request.user)
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data)

        

    def create(self, request):

        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass



    def partial_update(self, request, pk=None, model=None):
        
        model_object = self.get_object(pk)
        serializer = self.serializer(model_object, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def destroy(self, request, pk=None):
        instance = self.model.objects.get(id=pk)
        instance.delete()


        queryset = self.model.objects.filter(user = request.user)
        serializer = self.serializer(queryset, many=True)
        return Response(serializer.data) 


    def get_object(self, pk):
        return self.model.objects.get(pk=pk)
