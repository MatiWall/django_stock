from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from django.http import JsonResponse, HttpResponse

from django.template.loader import render_to_string

from django.db import connection
from django.custom_utils.utils import dictFetchAll
from django.core import serializers

from .models import tradingStrategyChoices, journalEntry


from .forms import journalEntryForm, journalEntryActionForm
# Create your views here.




class tradesView(TemplateView):
    template_name = 'journal/journalTrades.html'

    def get(self, request):

        return render(request, self.template_name, {})






class editView(TemplateView):
    template_name = "journal/editPage.html"

    def get(self, request):

        form = tradingStrategyChoicesForm()

        tsc_query = tradingStrategyChoices.objects.all()
        
        return render(request, self.template_name, {'form': form, 'tsc_query' :  tsc_query})


class tradeDetailView(TemplateView):
    template_name = 'journal/tradeDetail.html'

    def get(self, request):
        actionForm = journalEntryActionForm(request.user)

        return render( request, self.template_name, {'actionForm': actionForm})


class dashboardView(TemplateView):
    template_name = "journal/dashboardPage.html"

    def get(self, request):
    

        return render( request, self.template_name,{})







