import requests
import json


def loadData(tickersList, typesList):

    ticker = listToString(tickersList)
    types = listToString(typesList)

    token = "pk_1fabca50feb84a8a960fda5d63eeab29"
    
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/market/batch?symbols=" + ticker + "&types=" + types + "&token=" + token)
    
    try: 
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return api


def listToString(itemsList):
    '''
    makes it possible to get data in batches from api
    '''
      

    for i, item in enumerate(itemsList):
        if i == 0:
            items=str(item)
        else:
            items += "," + str(item)
    
    print(items)
    return items