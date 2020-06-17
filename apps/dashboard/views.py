from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.db import connection, transaction
from .models import dashboardGrid


from django.custom_utils.utils import dictFetchAll

from .fetchData.historicalData import getYahooData

import json
# Create your views here.





def dashboard(request):
    return render(request, 'dashboard/dashboardPage.html', {})





def save(request):

    if request.is_ajax() and request.method == 'PUT':
        data = json.loads(request.body) 

        cursor = connection.cursor()
            
        query = ''' 
                INSERT INTO dashboard_dashboardGrid
                    (grid_layout, name) VALUES (%s, %s) 
                ON CONFLICT (name) DO UPDATE   
                SET grid_layout = excluded.grid_layout
        '''
        
        cursor.execute(query, [ json.dumps(data) ,'Name Test7'])
    else:
        print('Error method not avalible: ' + request.method)


    return HttpResponse()





def load(request):



    if  request.method == 'GET': #and request.method == 'GET':
        cursor = connection.cursor()           
        query = ''' SELECT name FROM dashboard_dashboardGrid'''
        cursor.execute(query)
        rows = dictFetchAll(cursor)
        response = {'names' : rows}

    elif request.method == 'POST':
        name = json.loads(request.body)
        cursor = connection.cursor()
        query = ''' 
            SELECT grid_layout FROM dashboard_dashboardGrid WHERE name = %s
        '''
        cursor.execute(query, [name])
        positions = cursor.fetchone()[0]
        response = {'positions' :  positions}

    
    return JsonResponse(response)






def getHistoricalStockData(request):
    print('This ran')
    if  request.is_ajax() and request.method == 'POST':
        print('This ran')
        # Set IEX Finance API Token (Test)
        #os.environ['IEX_API_VERSION'] = 'iexcloud-sandbox'
        #os.environ['IEX_TOKEN'] = ''
        #print(os.environ)




        ohlc_data, volume_data = getYahooData('tsla')
        


        jsonData = {'ohlc' : ohlc_data, 'volume' : volume_data}
    return JsonResponse(jsonData)





