from django.shortcuts import render

from django.views.generic import TemplateView

from .forms import accountForm
from .models import accounts
# Create your views here.


class homeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get(self, request):

        form = accountForm()
        
        accounts_in_db = accounts.objects.all().order_by('-created')
        return render(request, self.template_name, {'form' : form, 'accounts':  accounts_in_db})

    def post(self, request):

        form = accountForm(data = request.POST)

        if form.is_valid():
            account = form.save(commit = False)
            account.user = request.user
            account.save()

        return render(request, self.template_name, {'form' : form})


    


