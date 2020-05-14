from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

from django.db import connection,transaction

from .models import dashboardGrid


from.loadData import loadData
from .webscraping import yhaooWebscraping, stockScreener
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



    tsla = stockScreener(['TSLA'])
    tsla.scrapeStocks()
    



    return render(request, 'home.html', {'currency' : currencyData ,'crypto' : cryptoData, 'commodity' : commodityData})
   


    


def about(request):
    return render(request, 'about.html', {})




def dashboard(request):
    return render(request, 'dashboard/dashboardPage.html', {})

def saveDashboard(request):
    import json

    if request.is_ajax() and request.method == 'PUT':
        data = json.loads(request.body) 

        cursor = connection.cursor()
            
        query = ''' INSERT INTO quotes_dashboardGrid
                    (grid_layout, name) VALUES
                    (%s, %s)

            '''
        cursor.execute(query, [ json.dumps(data) ,'Name Test4'])
    else:
        print('Error method not avalible: ' + request.method)


    return HttpResponse()

def loadDashboard(request):
    import json


    if  request.method == 'GET': #and request.method == 'GET':
        cursor = connection.cursor()           
        query = ''' SELECT name FROM quotes_dashboardGrid'''
        cursor.execute(query)
        rows = dictfetchall(cursor)
        response = {'names' : rows}
    
    return JsonResponse(response)






def fetchDashboardData(request):
   # import requests
    import json

    if  request.is_ajax():
        print(request.POST)
        data = json.loads(request.body)




        jsonData = json.dumps({'this' : 'Worked', 'Yes' : 'It fucking worked'})
    return HttpResponse(jsonData, status=200)





def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]

    data = [row[0] for row in cursor.fetchall() ]
    print(data)

    return data
    