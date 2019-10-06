# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:54:27 2019

@author: Richy
"""

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd 

# Make request to website and pull table
url = requests.get('https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/')

soup = bs(url.text, 'lxml')  

table = soup.find('table', {'border':'0'} )

yrs = table.find_all('tr')

# Extract contents of table
years = []
for yr in yrs:
    year = yr.contents[1].text
    Jan = yr.contents[3].text
    Feb = yr.contents[5].text
    Mar = yr.contents[7].text
    Apr =  yr.contents[9].text
    May =  yr.contents[11].text
    Jun =  yr.contents[13].text
    Jul =  yr.contents[15].text
    Aug =  yr.contents[17].text
    Sep =  yr.contents[19].text
    Oct =  yr.contents[21].text
    Nov = yr.contents[23].text
    Dec =  yr.contents[25].text
    An_AVG = yr.contents[27].text
    PerC_Dec = yr.contents[29].text
    #PerC_AVG = yr.contents[31].text
    years.append((year, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, An_AVG, PerC_Dec))#, PerC_AVG))
    
    
    
    
#Make dataframe and export as CSV    
df = pd.DataFrame(years, columns = years[1])
df = df.drop([0, 1])
df = df.set_index('Year')
df = df.replace(r'^\s*$', 0, regex=True)

#df.to_csv('cpi_per_year.csv', index = True, encoding='utf-8')
