import yfinance as yf
import pandas as pd 
import numpy as np


def getYahooData(ticker, start_date = None, end_date = None):

    ticker = yf.Ticker(ticker)

    if start_date is not None and end_date is not None:
        df = ticker.history(start = start_date, end = end_date, auto_adjust=True, back_adjust=False)
    else:
        df = ticker.history(period = 'max')

    df.index = df.index.astype(np.int64) / int(1e6)
    df.reset_index(inplace = True)
    
    ohlc_data = [[row['Date'], row['Open'], row['Close'], row['High'], row['Low']] for index, row in df.iterrows()]
    
    volume_data = [[row['Date'], row['Volume']] for index, row in df.iterrows()]
    

    return ohlc_data, volume_data


