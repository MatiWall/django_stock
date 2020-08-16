from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import JsonResponse, HttpResponse

from .models import journal


# Create your views here.






class tradesView(TemplateView):
    template_name = 'journal/journalTrades.html'

    def get(self, request):
        return render(request, self.template_name, {})





class dashboardView(TemplateView):
    template_name = "journal/dashboardPage.html"



class journalDetailView(TemplateView):
    template_name = "journal/journalDetailPage.html"

    def get(self, request):

        query = journal.objects.get(pk = 2 )    

        return render(request, self.template_name, {'journal' : query})
