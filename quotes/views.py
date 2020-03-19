from django.shortcuts import render, redirect
from django.contrib import messages

from .models import stockTickers
from .forms import stockForm
from.loadData import loadData
# Create your views here.


def login(request):
    return render(request, 'registration/login.html', {})


def home(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']
        api = loadData(ticker)
            
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker' : 'Enter a ticker'})
   


    


def about(request):
    return render(request, 'about.html', {})



def addStock(request):
    import requests
    import json
    if request.method == "POST":
        form = stockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock ticker has been addad"))
            return redirect('addStock')

    else:
        tickers_db = stockTickers.objects.all()
       
        api = loadData(tickers_db)
        
        return render(request, 'addStock.html', {'tickers': tickers_db,'api' : api})


def delete(request, stockId):
    item = stockTickers.objects.get(pk = stockId)
    item.delete()
    messages.success(request, ("Stock ticker has been deleted"))
    return redirect(addStock)

