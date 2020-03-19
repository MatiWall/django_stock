import requests
import json


def loadData(ticker):

    ticker = tickerToString(ticker)
    print(ticker)
    token = "pk_1fabca50feb84a8a960fda5d63eeab29"
    
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/market/batch?symbols=" + ticker + "&types=quote&token=" + token)
    
    try: 
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return api


def tickerToString(tickers_db):
    #tickers = [str(ticker) for ticker in tickers_db]
      
    tickers = ""

    for ticker in tickers_db:
        tickers += str(ticker) + ","
    
    return tickers