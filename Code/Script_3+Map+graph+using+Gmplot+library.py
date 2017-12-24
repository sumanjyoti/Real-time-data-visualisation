
# coding: utf-8

# In[1]:

# Heatmap

import gmplot

#gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

#gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
#gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
#gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
#gmap.heatmap(heat_lats, heat_lngs)

#gmap.draw("mymap.html")
#gmap = gmplot.GoogleMapPlotter("Ireland")


# In[2]:

# from -5 to 11

def get_color(temp = 4.0):
    if temp < -5.0:
        color = '#f7fbff'
    elif (temp < 0.0):
        color = '#ccebc5'
    elif temp < 1.0:
        color = '#a8ddb5'
    elif temp < 2.0:
        color = '#7bccc4'
    elif temp < 3.0:
        color = '#4eb3d3'
    elif temp < 4.0:
        color = '#2b8cbe'
    elif temp < 5.0:
        color = '#0868ac'
    else:
        color = '#084081'
    return color
#get_color()
#ccebc5
#a8ddb5
#7bccc4
#4eb3d3
#2b8cbe
#0868ac
#084081



# In[3]:

import json
#open('Ireland.json')
with open('Ireland.json', 'r') as f:
    datastore = json.load(f)
    
import pandas as pd
def get_recent_data(file = 'Temprature'):
    df = pd.read_csv(file+'.csv')
    return df.tail(1)
recent_data = get_recent_data()
#recent_data
#print(recent_data['Waterford'].values[0])
#get_color(recent_data['Waterford'].values[0])


# In[4]:

var_1 = 0
var_2 = 0
    #hash
map_arr = []
datastore_features = datastore['features']
for var_1 in datastore_features:
    lats_for_one_city = []
    lons_for_one_city = []
    map_city = var_1['id']
    #print(recent_data[map_city])
    color = get_color(recent_data[map_city].values[0])
    temp = recent_data[map_city].values[0]
    cords = var_1['geometry']['coordinates'][0]
    for var_2 in cords:
        lats_for_one_city.append(var_2[1])
        lons_for_one_city.append(var_2[0])
    #print(lats_for_one_city)
    map_arr.append([map_city,lats_for_one_city,lons_for_one_city,color,temp])


# In[5]:

import gmplot
#map_arr = [['Dublin',[52.708085,52.924335,52.633128],[-6.592415,-6.712332,-6.71789]],
#            ['Cork',[52.708085,52.924335,52.633128],[-6.592415,-6.712332,-6.71789]],
#            ['ABC',[52.708085,52.924335,52.633128],[-6.592415,-6.712332,-6.71789]]
#           ]
# for cods in map_arr:
#     print(cods)


def make_map(map_arr):
    gmap = gmplot.GoogleMapPlotter(52.708085, -6.592415, 6)
#lats = heat_lats = marker_lats = more_lats = latitudes = [52.708085,52.924335,52.633128]
#lngs = heat_lngs = marker_lngs = more_lngs = longitudes = [-6.592415,-6.712332,-6.71789]
    for cods in map_arr:
        lats = heat_lats = marker_lats = more_lats = latitudes = cods[1]
        lngs = heat_lngs = marker_lngs = more_lngs = longitudes = cods[2]
        #gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
        #gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
        #gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
        #gmap.heatmap(heat_lats, heat_lngs)
        gmap.polygon(lats, lngs, color = cods[3], c=cods[3],facecolor= cods[3],clickable=True,title = 'Temprature')
        #gmap.marker(lats[1], lngs[1], title= cods[4])
    gmap.draw("mymap.html")

make_map(map_arr)

