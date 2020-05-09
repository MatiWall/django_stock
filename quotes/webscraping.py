import pandas as pd
import requests
from bs4 import BeautifulSoup

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

    



    


    