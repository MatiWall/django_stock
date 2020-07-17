from django.http import HttpResponse, JsonResponse
from django.core import serializers 

from django.views import View

from .forms import tradingStrategyChoicesForm, journalEntryForm

from django.custom_utils.utils import cleanFormData

from .models import journalEntry

import json


class homeTableView(View):

    def get(self, request):

        
        serialized_objects= serializers.serialize("json", journalEntry.objects.filter(user = request.user))
        
       

        json_objects=json.loads(serialized_objects)
        list_objects = []   
        for row in json_objects:
            data = row['fields']
            data['pk'] = row['pk']    
            list_objects.append(data)
    
        
        return HttpResponse(json.dumps(list_objects), content_type='application/json;charset=utf-8')




def journalFormView(request):

    if request.method == 'POST':
        response = 'Invalid'

        try:
            data = json.loads(request.body)   
            data = cleanFormData(data)
            form = journalEntryForm(request.user, data = data )

        except:
            response = 'Load data error'

        
    
        
        if form.is_valid():
            
            entry = form.save(commit = False)
            entry.user = request.user
            entry.save()

            response = 'Journal Entry Saved'
        else:
            response = form.errors
            print(response)
            
        
        return JsonResponse({'res' : response})




