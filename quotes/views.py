from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse


from.loadData import loadData
from .webscraping import yhaooWebscraping
# Create your views here.


def login(request):
    return render(request, 'registration/login.html', {})


def home(request):

    currencyUrl = 'https://finance.yahoo.com/currencies?.tsrc=fin-srch'
    currency = yhaooWebscraping(currencyUrl)
    currencyData = currency.get_html()


    cryptoUrl = 'https://finance.yahoo.com/cryptocurrencies?.tsrc=fin-srch'
    crypto = yhaooWebscraping(cryptoUrl)
    cryptoData = crypto.get_html()

    commodityUrl = 'https://finance.yahoo.com/commodities?.tsrc=fin-srch'
    commodity = yhaooWebscraping(commodityUrl)
    commodityData = commodity.get_html()



    return render(request, 'home.html', {'currency' : currencyData ,'crypto' : cryptoData, 'commodity' : commodityData})
   


    


def about(request):
    return render(request, 'about.html', {})




def dashboard(request):
    return render(request, 'dashboard/dashboardPage.html', {})


def fetchDashboardData(request):
   # import requests
    import json

    if request.is_ajax():
        print(request.POST)
        data = json.loads(request.body)




        jsonData = json.dumps({'this' : 'Worked', 'Yes' : 'It fucking worked'})
    return HttpResponse(jsonData, status=200)



