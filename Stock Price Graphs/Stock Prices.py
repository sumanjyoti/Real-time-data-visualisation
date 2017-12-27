
# coding: utf-8

# In[193]:




#Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import plotly
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
import time 
import  pandas_datareader as web
# Package and modules for importing data;
import datetime
import requests
import json as js
import csv



# In[195]:




# Calling API for Microsoft stock prices

headers = {
    'X-API-KEY': 'Get API key',
}
API_KEY = 'Get API key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file1 = api_call.text
file1=js.loads(api_call.text)



# In[197]:




file1['Time Series (Daily)']['2017-07-27']



# In[198]:




# To write into csv

from datetime import datetime

csv.writer(open("data.csv", "wb"), dialect="excel")

x = file1

#f = csv.writer(open("abc.csv", ""))

# Write CSV Header, If you dont need that, remove this line
#f.writerow(["pk", "model", "codename", "name", "content_type"])
temp_data = file1['Time Series (Daily)']
with open('Microsoft_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Microsoft_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[199]:




# Changing time to Day Month Year format
temp_data = file1['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[200]:




Microsoft.dropna(inplace=True)
Microsoft=pd.read_csv('Microsoft_stock.csv', parse_dates=True, index_col=0 )
print(Microsoft.head(5))



# In[201]:




Microsoft.index.values



# In[202]:




#Cleaning the index values. Changing time to Day Month Year format
Address_M='Microsoft_stock.csv'
Microsoft=pd.read_csv(Address_M)
Microsoft['Date'] = pd.to_datetime(Microsoft['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[203]:




Microsoft[['High','Low']].plot()
plt.show()
print()



# In[204]:




a=Microsoft['Date']
b=Microsoft['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Microsoft')



# In[205]:




# Calling API for Apple's stock prices

headers = {
    'X-API-KEY': 'Get api key ',
}
API_KEY = 'Get api key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=ful&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file2 = api_call.text
file2=js.loads(api_call.text)



# In[206]:




# To write into csv

csv.writer(open("data.csv", "wb"), dialect="excel")

x = file2

temp_data = file2['Time Series (Daily)']
with open('Apple_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Apple_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[207]:




# Changing time to Day Month Year format
temp_data = file2['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[208]:




Apple.dropna(inplace=True)
Apple=pd.read_csv('Apple_stock.csv', parse_dates=True, index_col=0 )



# In[209]:




#Cleaning the index values. Changing time to Day Month Year format
Address_A='Apple_stock.csv'
Apple=pd.read_csv(Address_A)
Apple['Date'] = pd.to_datetime(Apple['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[210]:




a=Apple['Date']
b=Apple['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Apple')



# In[211]:




# Calling API for Facebook stock prices

headers = {
    'X-API-KEY': 'Get API key',
}
API_KEY = 'Get API key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=FB&outputsize=full&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file3 = api_call.text
file3=js.loads(api_call.text)



# In[212]:




# To write into csv

csv.writer(open("data.csv", "wb"), dialect="excel")

x = file3

temp_data = file3['Time Series (Daily)']
with open('Facebook_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Facebook_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[213]:




# Changing time to Day Month Year format
temp_data = file3['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[214]:




Facebook = pd.read_csv('Facebook_stock.csv', parse_dates=True, index_col=0 )
Facebook.dropna(inplace=True)



# In[215]:




#Cleaning the index values. Changing time to Day Month Year format
Address_F='Facebook_stock.csv'
Facebook=pd.read_csv(Address_F)
Facebook['Date'] = pd.to_datetime(Facebook['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[216]:




a=Facebook['Date']
b=Facebook['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Facebook')



# In[217]:




# Calling API for Google stock prices
headers = {
    'X-API-KEY': 'Get API key',
}
API_KEY = 'Get API key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOG&outputsize=full&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file4 = api_call.text
file4=js.loads(api_call.text)
a=file4['Time Series (Daily)']



# In[218]:




x = file4

temp_data = file4['Time Series (Daily)']
with open('Google_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Google_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[219]:




# Changing time to Day Month Year format
temp_data = file4['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[220]:




Google = pd.read_csv('Google_stock.csv', parse_dates=True, index_col=0 )
Google.dropna(inplace=True)



# In[221]:




#Cleaning the index values. Changing time to Day Month Year format
Address_G='Google_stock.csv'
Google=pd.read_csv(Address_G)
Google['Date'] = pd.to_datetime(Google['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[222]:




a=Google['Date']
b=Google['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Google')



# In[224]:




# Calling API for Disney stock prices

headers = {
    'X-API-KEY': 'Get API key',
}
API_KEY = 'Get API key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=DIS&outputsize=full&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file5 = api_call.text
file5=js.loads(api_call.text)



# In[225]:




# To write into csv

csv.writer(open("data.csv", "wb"), dialect="excel")

x = file5

temp_data = file5['Time Series (Daily)']
with open('Disney_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Disney_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[226]:




# Changing time to Day Month Year format
temp_data = file5['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[227]:




Disney = pd.read_csv('Disney_stock.csv', parse_dates=True, index_col=0 )
Disney.dropna(inplace=True)



# In[228]:




#Cleaning the index values. Changing time to Day Month Year format
Address_D='Disney_stock.csv'
Disney=pd.read_csv(Address_D)
Disney['Date'] = pd.to_datetime(Disney['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[230]:




a=Disney['Date']
b=Disney['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Disney')



# In[231]:




# Calling API for Netflix stock prices

headers = {
    'X-API-KEY': 'Get API key',
}
API_KEY = 'Get API key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NFLX&outputsize=full&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file6 = api_call.text
file6=js.loads(api_call.text)



# In[232]:




# To write into csv

csv.writer(open("data.csv", "wb"), dialect="excel")

x = file6

temp_data = file6['Time Series (Daily)']
with open('Netflix_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Netflix_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[233]:




# Changing time to Day Month Year format
temp_data = file6['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[234]:




Netflix = pd.read_csv('Netflix_stock.csv', parse_dates=True, index_col=0 )
Netflix.dropna(inplace=True)



# In[235]:




#Cleaning the index values. Changing time to Day Month Year format
Address_N='Netflix_stock.csv'
Netflix=pd.read_csv(Address_N)
Netflix['Date'] = pd.to_datetime(Netflix['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[236]:




a=Netflix['Date']
b=Netflix['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Netflix')



# In[237]:




# Calling API for Amazon stock prices

headers = {
    'X-API-KEY': 'Get API key',
}
API_KEY = 'Get API key'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&outputsize=full&apikey='+API_KEY
api_call=requests.get(url, headers=headers)
file7 = api_call.text
file7 =js.loads(api_call.text)



# In[238]:




# To write into csv

csv.writer(open("data.csv", "wb"), dialect="excel")

x = file7

temp_data = file7['Time Series (Daily)']
with open('Amazon_stock.csv','w') as f:
    writ =  csv.writer(f)
    label=('Date','Open','High','Low','Close','Volume')
    writ.writerow(label)
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    fields =[datetime_object,
             float(temp_data[temp_date]['1. open']),
             float(temp_data[temp_date]['2. high']),
             float(temp_data[temp_date]['3. low']),
             float(temp_data[temp_date]['4. close']),
             float(temp_data[temp_date]['5. volume'])]
#     print (fields)
    with open('Amazon_stock.csv','a') as f:
        writ =  csv.writer(f)
        writ.writerow(fields)
        
        


# In[239]:




# Changing time to Day Month Year format
temp_data = file7['Time Series (Daily)']
for temp_date in temp_data:
    datetime_object = datetime.strptime(temp_date, '%Y-%m-%d')
    (datetime_object)
    
    


# In[240]:




Amazon = pd.read_csv('Amazon_stock.csv', parse_dates=True, index_col=0 )
Amazon.dropna(inplace=True)



# In[241]:




#Cleaning the index values. Changing time to Day Month Year format
Address_A='Amazon_stock.csv'
Amazon=pd.read_csv(Address_A)
Amazon['Date'] = pd.to_datetime(Amazon['Date']).apply(lambda x: x.strftime('%Y-%m-%d')if not pd.isnull(x) else '')



# In[242]:




a=Amazon['Date']
b=Amazon['High']

trace= go.Scatter(x=a,y=b)
data=[trace]
py.iplot(data, filename='Amazon')



# In[243]:



# calling plotly with api
plotly.tools.set_credentials_file(username='zahras', api_key='Get PLotly API key')



# In[244]:




#Plotting date vs highest stock price for Microsoft, Apple and Tesla from 2005 to today

Microsoft_plot=go.Scatter(
    x=Microsoft['Date'],
    y=Microsoft['High'],
    name='Microsoft')

Apple_plot=go.Scatter(
    x=Apple['Date'],
    y=Apple['High'],
    name='Apple')

Facebook_plot=go.Scatter(
    x=Facebook['Date'],
    y=Facebook['High'],
    name='Facebook')

Google_plot=go.Scatter(
    x=Google['Date'],
    y=Google['High'],
    name='Tesla')

Disney_plot=go.Scatter(
    x=Disney['Date'],
    y=Disney['High'],
    name='Disney')

Netflix_plot=go.Scatter(
    x=Netflix['Date'],
    y=Netflix['High'],
    name='Netflix')



Amazon_plot=go.Scatter(
    x=Amazon['Date'],
    y=Amazon['High'],
    name='Amazon')


data = [Microsoft_plot, Apple_plot, Facebook_plot, Google_plot, Disney_plot, Netflix_plot, Amazon_plot]
layout=go.Layout(barmode='bar')

Fig=go.Figure(data=data,layout=layout)
py.iplot(Fig,filename='Stock Prices')


# In[245]:


import plotly as py
import plotly.graph_objs as go
import ipywidgets as widgets

py.offline.init_notebook_mode(connected=True)

#Plotting date vs highest stock price for Microsoft, Apple and Tesla from 2005 to today


def graph_data(graph_name):
    Microsoft_plot=go.Scatter(
    x=Microsoft['Date'],
    y=Microsoft[graph_name],
    name='Microsoft')
        
    Apple_plot=go.Scatter(
    x=Apple['Date'],
    y=Apple[graph_name],
    name='Apple')


    Facebook_plot=go.Scatter(
    x=Facebook['Date'],
    y=Facebook[graph_name],
    name='Facebook')

    Google_plot=go.Scatter(
    x=Google['Date'],
    y=Google[graph_name],
    name='Tesla')

    Disney_plot=go.Scatter(
    x=Disney['Date'],
    y=Disney[graph_name],
    name='Disney')

    Netflix_plot=go.Scatter(
    x=Netflix['Date'],
    y=Netflix[graph_name],
    name='Netflix')

    Amazon_plot=go.Scatter(
    x=Amazon['Date'],
    y=Amazon[graph_name],
    name='Amazon')    
    
    data=[Microsoft_plot, Apple_plot, Facebook_plot, Google_plot, Disney_plot, Netflix_plot, Amazon_plot]
    layout=go.Layout(barmode='bar')

    Fig=go.Figure(data=data,layout=layout)
    py.offline.iplot(Fig,filename='Stock Prices')

# graph_data('High') 



graph_type = ['High', 'Low', 'Open', 'Close', 'Volume']
signal = widgets.Select(options=graph_type,value='High',description='Values',disable = False)
widgets.interactive(graph_data,graph_name = signal)

