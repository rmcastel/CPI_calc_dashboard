# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:09:47 2019

@author: Richy
"""

import pandas as pd 

df = pd.read_csv(r"C:\Users\Richy\Documents\Python Scripts\Web scrapes\CPI\cpi_per_year.csv", encoding = 'utf8')

df = df.set_index('Year')


def purchasing_power(price, year_assoc_with_price, year_of_interest, month):
    if year_assoc_with_price > 2018 or year_assoc_with_price < 1913:
        raise ValueError('No CPI information for given year (2nd argument)')
    elif year_of_interest > 2018 or year_of_interest < 1913:
        raise ValueError('No CPI information for given year (3rd argument)')
    else:
        pp = (df.loc[year_of_interest, month] / df.loc[year_assoc_with_price, month]) * price
        
    print('${:,.2f}'.format(price), 'in', year_assoc_with_price, 'is equivalent to', '${:,.2f}'.format(pp), 'in', year_of_interest)
    return pp, year_assoc_with_price, year_of_interest


print(purchasing_power(200, 2018, 1913, 'Oct'))