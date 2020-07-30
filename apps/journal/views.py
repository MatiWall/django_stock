from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import JsonResponse, HttpResponse



# Create your views here.




class tradesView(TemplateView):
    template_name = 'journal/journalTrades.html'





class dashboardView(TemplateView):
    template_name = "journal/dashboardPage.html"






