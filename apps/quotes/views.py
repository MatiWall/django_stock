from django.shortcuts import render, redirect
#from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
#from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import update_session_auth_hash

from django.http import HttpResponse, JsonResponse

from django.db import connection, transaction


from.loadData import loadData
from .webscraping import yhaooWebscraping, stockScreener

from iexfinance.stocks import Stock, get_historical_data
from datetime import datetime

import json
import os
# Create your views here.


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



    tsla = stockScreener(['TSLA'])
    tsla.scrapeStocks()
    



    return render(request, 'home.html', {'currency' : currencyData ,'crypto' : cryptoData, 'commodity' : commodityData})
   


    


def about(request):
    return render(request, 'about.html', {})


