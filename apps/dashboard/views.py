from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.db import connection, transaction
from .models import dashboardGrid

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
        rows = dictfetchall(cursor)
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






def fetchData(request):
    
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
    