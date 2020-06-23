from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import dashboardComponentOptions
from .forms import historicalDataOptions

from django.template import loader

from django.custom_utils.utils import cleanFormData
import json


from .fetchData.historicalData import getYahooData






def chartOptionsForm(request, chartType):

    form = historicalDataOptions()
    
    
    return JsonResponse({'form' : form.as_p()})



def chartOptionsChosen(request):
    
    if request.method == 'POST' and request.is_ajax():
        
        optionsForm = cleanFormData(json.loads(request.body))
   
        
        ohlc_data, volume_data = getYahooData('tsla', start_date = optionsForm['start_date'], end_date = optionsForm['end_date'])
        
        jsonData = {'ohlc' : ohlc_data, 'volume' : volume_data}
  

    return JsonResponse(jsonData)


