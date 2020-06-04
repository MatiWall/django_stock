from django.shortcuts import render
from django.db import connection

from .models import accounts, positions
from .forms import accountForm, positionForm

from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize

from django.custom_utils.utils import cleanFormData

import json
import pandas as pd



def position_view(request):
    if request.method == 'POST' and request.is_ajax():
        try:
            data = json.loads(request.body)   
            data = cleanFormData(data)
            PositionForm = positionForm(data = data)

        except:
            print('Data load error')
            return HttpResponse('Data load error')
            

        
        if PositionForm.is_valid():
            position = PositionForm.save(commit = False)
            position.user = request.user
            position.save()

    


        return JsonResponse({'data' : getPositions(request).to_html().replace('class="dataframe"','class=""')})


    return HttpResponse('Error')




def getPositions(request):
    '''
    Retrives the current users stock positions from the database and returns a DataFrame
    '''
    positions_in_db = positions.objects.filter(user_id = request.user.id)
    positions_serialize = json.loads(serialize('json', positions_in_db))
    print(positions_in_db)
    positions_list = []
    for row in  positions_serialize:
        fields = row['fields']
        fields['account_name'] = getAccountName(fields['account'])
        positions_list.append(fields)
    
    return pd.DataFrame(positions_list )   


def getAccountName(id):
    account = accounts.objects.raw('SELECT id, name FROM portfolio_accounts where id = %s', [id])
    return account[0].name