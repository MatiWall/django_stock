import pandas as pd
import requests

import time
from bs4 import BeautifulSoup


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import geckodriver_autoinstaller
geckodriver_autoinstaller.install()

#from multiprocessing.dummy import Pool as ThreadPool 

#import json

#from tidylib import tidy_document # for tidying incorrect html





class yhaooWebscraping:

    def __init__(self, url):
        self.url = url

     
        site = requests.get(self.url)
        data = site.text
        soup = BeautifulSoup(data, 'html.parser')

        names = []

        header = soup.find('table').find('thead').find_all('th')
        
        for cell in header:
            names.append(cell.get_text())
        self.df = pd.DataFrame(columns = names[1:-2])

        rows = soup.find('table').find('tbody').find_all('tr')
        for row in rows: 
            table_row = []

            cells = row.find_all("td")
            for cell in cells:
                value = cell.get_text()
                table_row.append(value)
        
            self.df.loc[len(self.df)] = table_row[1:-2]
        
        self.df.index = self.df.index+1

    def get_data(self):
        return self.df
    
    def get_sorted_date(self):
        return self.df.sort_values(ascending = False)

    def get_html(self):
        return self.df.to_html()

    



class stockScreener:

    def __init__(self, tickers):
        self.tickers = tickers
        self.baseURL = 'https://finance.yahoo.com/quote/'
        self.indicators = []


        
    def scrapeStocks(self):

        for i, ticker in enumerate(self.tickers):
            valuationMeasures, FH_TI = self.scrape(ticker)

            if i == 0:
                self.indicators = FH_TI.index.to_list() + valuationMeasures.index.to_list()

    
    def scrape(self, ticker):
        url = self.baseURL + ticker + '/key-statistics?p=' +ticker
            

        options = Options()
        options.headless = True 
        driver = webdriver.Firefox(options = options)
          
                        
        driver.get(url)
        driver.implicitly_wait(100)

        # Have to click cookie button
        driver.find_element_by_css_selector('.btn.primary').click()
        time.sleep(1)

            
        soup = BeautifulSoup(driver.page_source, 'html.parser')
             
        data = soup.find('div', {'class' : 'Mstart(a) Mend(a)', 'data-reactid' : '11'})
        for tag in data.findAll('sup'):
            tag.replaceWith('')
            
        frames = pd.read_html(str(data))
        series = pd.Series()
        for frame in frames:
            frame.set_index(frame.columns[0], inplace = True)
            if isinstance(frame, pd.DataFrame) and frame.shape[1]>1:
                df = frame
            elif isinstance(frame, pd.DataFrame) and frame.shape[1]==1:
                series = series.append(frame.iloc[:,0])
  
        
        return df, series


    def get_indicators(self):
        return self.indicators
            
        





    


    