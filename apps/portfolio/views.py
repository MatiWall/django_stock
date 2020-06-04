from django.shortcuts import render
from django.db import connection

from django.views.generic import TemplateView

from .forms import accountForm, positionForm
from .models import accounts, positions




# Create your views here.


class homeView(TemplateView):
    template_name = 'portfolio/home.html'

  

    def get(self, request):
        user_accounts = accounts.objects.raw('SELECT * FROM portfolio_accounts WHERE user_id = %s ORDER BY created', [request.user.id])

        AccountForm = accountForm()
        PositionForm = positionForm()
        return render(request, self.template_name, {'accountForm' : accountForm, 'accounts':  user_accounts, 'positionForm': PositionForm})

    def post(self, request):
        
        form = accountForm(data = request.POST)
        user_accounts = accounts.objects.raw('SELECT * FROM portfolio_accounts WHERE user_id = %s ORDER BY created', [request.user.id])
        

        if form.is_valid():
            account = form.save(commit = False)
            account.user = request.user
            account.save()

        return render(request, self.template_name, {'form' : form, 'accounts':  user_accounts})


    


