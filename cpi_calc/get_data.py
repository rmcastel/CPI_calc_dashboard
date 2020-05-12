# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:37:50 2020

@author: Richy
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_data():
    '''
    Function to pull data from internet
    '''
    r = requests.get('https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/')
    soup = BeautifulSoup(r.text, 'lxml')
    table = soup.find('table', {'border':'0'})
    yrs = table.find_all('tr')

    # Extract contents of table
    years = []
    for yr in yrs[:-1]: #yrs[-1] to remove the year 2020, 
        year = yr.contents[1].text
        Jan = yr.contents[3].text
        Feb = yr.contents[5].text
        Mar = yr.contents[7].text
        Apr = yr.contents[9].text
        May = yr.contents[11].text
        Jun = yr.contents[13].text
        Jul = yr.contents[15].text
        Aug = yr.contents[17].text
        Sep = yr.contents[19].text
        Oct = yr.contents[21].text
        Nov = yr.contents[23].text
        Dec = yr.contents[25].text
        Avg = yr.contents[27].text
        #Perc_Dec = yr.contents[29].text
        #PerC_AVG = yr.contents[31].text
        years.append((year, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec, Avg)) #, Perc_Dec))

    #Make dataframe and export as CSV
    df = pd.DataFrame(years, columns=years[1])
    df = df.drop([0, 1])
    df = df.apply(pd.to_numeric)
    df = df.set_index('Year')
    #df = df.replace(r'^\s*$', 0, regex=True)

    return df


df = get_data()