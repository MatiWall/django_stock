from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from django.http import JsonResponse, HttpResponse

from django.template.loader import render_to_string

from django.db import connection
from django.custom_utils.utils import dictFetchAll
from django.core import serializers

from .models import tradingStrategyChoices, journalEntry


from .forms import journalEntryForm
# Create your views here.




class homeView(TemplateView):
    template_name = "journal/journalPage.html"

    def get(self, request):

        form = journalEntryForm(request.user)

        return render(request, self.template_name, {'form' : form})






class editView(TemplateView):
    template_name = "journal/editPage.html"

    def get(self, request):

        form = tradingStrategyChoicesForm()

        tsc_query = tradingStrategyChoices.objects.all()
        
        return render(request, self.template_name, {'form': form, 'tsc_query' :  tsc_query})


class tradesView(TemplateView):
    template_name = 'journal/tradesPage.html'





def dashboardView(request):
    template_name = "journal/dashboardPage.html"

    html = render_to_string( template_name, {})
    
    return HttpResponse(html)

