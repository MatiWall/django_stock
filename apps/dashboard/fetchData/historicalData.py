import yfinance as yf
import pandas as pd 
import numpy as np


def getYahooData(ticker, range=None):

    ticker = yf.Ticker(ticker)

    if range is not None:
        df = ticker.history(start = range['start'], end = range['end'], auto_adjust=True, back_adjust=False)
    else:
        df = ticker.history(period = 'max')

    df.index = df.index.astype(np.int64) / int(1e6)
    df.reset_index(inplace = True)
    
    ohlc_data = [[row['Date'], row['Open'], row['Close'], row['High'], row['Low']] for index, row in df.iterrows()]
    
    volume_data = [[row['Date'], row['Volume']] for index, row in df.iterrows()]
    

    return ohlc_data, volume_data


