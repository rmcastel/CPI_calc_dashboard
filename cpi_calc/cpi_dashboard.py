# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:08:39 2019

@author: Richy
"""

#pip install dash==0.21.1  
#pip install dash-renderer==0.13.0  
#pip install dash-html-components==0.11.0
#pip install dash-core-components==0.23.0  
#pip install plotly --upgrade



import dash 
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output

import pandas as pd 

path = r"C:\Users\Richy\Documents\Python Scripts\Web scrapes\CPI\cpi_per_year.csv"
df = pd.read_csv(path, encoding = 'utf8')

df = df.set_index('Year')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H1(children = 'CPI Calculator', style={'textAlign': 'center', 'color': colors['text']}),
    
    html.H3(children = '*Year Must Be Between 1913 & 2019', style={'textAlign': 'center'}),
    
    html.Div([
        html.Label('Price ($): '),
        dcc.Input(id = 'Price', type = 'number', value= 100, style = {'textAlign' : 'center'})], style = {'textAlign' : 'center', 'padding': 10}),

    html.Div([
            html.Label(' Year of Price: ', style = {'textAlign' : 'center'}),
            dcc.Input(id='P_Year', type='number', value = 2018, style = {'textAlign' : 'center'})], style = {'textAlign' : 'center'}),

    html.Div([
            html.Label(' Year of Interest: ', style = {'textAlign' : 'center'}),
            dcc.Input(id = 'I_Year', type = 'number', value = 1995, style = {'textAlign' : 'center'})], style = {'textAlign' : 'center', 'padding': 10}),
    html.Div([
            html.Label(' Yearly Average or Month: ', style = {'textAlign' : 'center'}),
            dcc.Dropdown(
                        id = 'months',
                    	options = [
                    		{'label' : 'Average', 'value': 'Avg' },
                    		{'label' : 'January', 'value': 'Jan' },
                    		{'label' : 'February', 'value': 'Feb' },
                    		{'label' : 'March', 'value': 'Mar' },
                    		{'label' : 'April', 'value': 'Apr' },
                    		{'label' : 'May', 'value': 'May' },
                    		{'label' : 'June', 'value': 'June' },
                    		{'label' : 'July', 'value': 'July' },
                    		{'label' : 'August', 'value': 'Aug' },
                    		{'label' : 'September', 'value': 'Sep' },
                    		{'label' : 'October', 'value': 'Oct' },
                    		{'label' : 'November', 'value': 'Nov' },
                    		{'label' : 'December', 'value': 'Dec' }
                    	],
                        value = 'Avg',
                    	searchable = True)], style = {'textAlign' : 'center', 'padding': 10}),
    html.Div(id='my-div', style = {'textAlign' : 'center'})
])
    


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='Price', component_property='value'),
     Input('P_Year', 'value'),
     Input('I_Year', 'value'),
     Input('months', 'value')]
)

def purchasing_power(price, year_assoc_with_price, year_of_interest, month):
    if year_assoc_with_price > 2019 or year_assoc_with_price < 1913:
        return 'No CPI information for given year (2nd argument)'
    elif year_of_interest > 2019 or year_of_interest < 1913:
        return 'No CPI information for given year (3rd argument)'
    else:
        pp = (df.loc[year_of_interest, month] / df.loc[year_assoc_with_price, month]) * price        
        if month == 'Avg':
            return '${:,.2f}'.format(price), ' in ', year_assoc_with_price, ' is equivalent to ', '${:,.2f}'.format(pp), ' in ', year_of_interest 
        else:
            if df.loc[year_assoc_with_price, month] == 0:
                return 'Data for this months CPI has not been reported yet'
            return '${:,.2f}'.format(price), ' in ', month, ' ',  year_assoc_with_price, ' is equivalent to ', '${:,.2f}'.format(pp), ' in ', month, ' '    , year_of_interest


if __name__ == '__main__':
    app.run_server(debug = True)
    


##########################################
## to run open python prompt and run    ##
## python cpi_dashboard.py, then visit  ##
##      http://127.0.0.1:8050           ##
##########################################