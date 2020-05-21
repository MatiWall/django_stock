from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse

from django.db import connection,transaction

from .models import dashboardGrid


from.loadData import loadData
from .webscraping import yhaooWebscraping, stockScreener

from iexfinance.stocks import Stock, get_historical_data
from datetime import datetime

import json
import os
# Create your views here.


def userSignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
    else: 
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form' : form} )


def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        
        if form.is_valid():

            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')

    elif request.method == 'GET':
        form = AuthenticationForm()
        

    return render(request, 'registration/login.html', {'form' : form})

def userLogout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/userLogin/')

    pass


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



@login_required(login_url='/userLogin/')
def dashboard(request):
    return render(request, 'dashboard/dashboardPage.html', {})

def saveDashboard(request):

    if request.is_ajax() and request.method == 'PUT':
        data = json.loads(request.body) 

        cursor = connection.cursor()
            
        query = ''' 
                INSERT INTO quotes_dashboardGrid
                    (grid_layout, name) VALUES (%s, %s) 
                ON CONFLICT (name) DO UPDATE   
                SET grid_layout = excluded.grid_layout
        '''
        
        cursor.execute(query, [ json.dumps(data) ,'Name Test7'])
    else:
        print('Error method not avalible: ' + request.method)


    return HttpResponse()

def loadDashboard(request):



    if  request.method == 'GET': #and request.method == 'GET':
        cursor = connection.cursor()           
        query = ''' SELECT name FROM quotes_dashboardGrid'''
        cursor.execute(query)
        rows = dictfetchall(cursor)
        response = {'names' : rows}

    elif request.method == 'POST':
        name = json.loads(request.body)
        cursor = connection.cursor()
        query = ''' 
            SELECT grid_layout FROM quotes_dashboardGrid WHERE name = %s
        '''
        cursor.execute(query, [name])
        positions = cursor.fetchone()[0]
        response = {'positions' :  positions}

    
    return JsonResponse(response)






def fetchDashboardData(request):
    
    if  request.is_ajax() and request.method == 'POST':
        
        os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'
        os.environ['IEX_TOKEN'] = 'Tpk_1d9ebd084c5149d79631fa7cbf811a8e'
        
        tsla = get_historical_data("TSLA", datetime(2015, 1, 1), datetime(2015, 1,31) ) 
        print(tsla)

        data = json.loads(request.body)
        # Set IEX Finance API Token (Test)
        #os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'
        #os.environ['IEX_TOKEN'] = ''
        #print(os.environ)




        jsonData = {'this' : 'Worked', 'Yes' : 'It fucking worked'}
    return JsonResponse(jsonData)





def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]

    data = [row[0] for row in cursor.fetchall() ]

    return data
    