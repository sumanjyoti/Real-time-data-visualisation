
# coding: utf-8

# In[1]:

##########################################################################################################################
#https://plot.ly/streaming/ 
import plotly as py
import plotly.graph_objs as go
import ipywidgets as widgets
import numpy as np
import datetime
py.offline.init_notebook_mode(connected=True)   # for offline mode use


# In[2]:

#########################################################################################################################
# Reading data from File 
import pandas as pd

def get_file(file = 'Temprature'):
    df = pd.read_csv(file+'.csv')
    cities = (list(df.columns.values))[1:]
    return df,cities
#df,cities = get_file('Temprature')
#df
#cities


# In[3]:

##########################################################################################################################
# x is date
def graph_data(graph_name = 'Temprature'):
    df,cities = get_file(graph_name)
    x = df['DateTime']
    layout = go.Layout(
        title='<b> '+graph_name+' Graph </b>',
        yaxis=dict(
            title='<i>('+graph_name+')</i>'
        ),
        xaxis=dict(
            title='<i>(Time)</i>'
        )
    )
    trace = []
    for city in cities:
        trace1 = go.Scatter(
            x = x,
            y = df[city],
            mode = 'lines',
            name = city+' '+graph_name,
            line = dict(
                shape = 'spline'
            )
        )
        trace.append(trace1)
#cities = (list(df.columns.values))[1:]
    fig = go.Figure(data =trace,layout =layout)
    py.offline.iplot(fig)


# In[4]:

##########################################################################################################################
graph_types = ['Temprature','Pressure','Humidity','Wind_Speed']   
signal1 = widgets.Select(options=graph_types, value='Temprature' , description='Graph Types', disabled=True)
widgets.interactive(graph_data, graph_name=signal1)
#graph_data()


# In[6]:

#########################################################################################################################
def box_plot_graph(graph_name):
    df,cities = get_file(graph_name)
    y0 = df[cities[1]]
    y1 = df[cities[2]]
    trace = []
    x = cities
    for city in cities:
        trace1 = go.Box(
            y = df[city],
            name = city,
        )
        trace.append(trace1)
    layout = go.Layout(
        xaxis=dict( 
            title = graph_name
                  ),
        yaxis=dict(
            title = 'city' 
        )
    )
    py.offline.iplot(trace)
########################################################################################################################


# In[8]:

#box_plot_graph('Wind_Speed')
#graph_data()
graph_types = ['Temprature','Pressure','Humidity','Wind_Speed']   
signal1 = widgets.Select(options=graph_types, value='Humidity' , description='Graph Types', disabled=True)
widgets.interactive(box_plot_graph, graph_name=signal1)


# In[ ]:



