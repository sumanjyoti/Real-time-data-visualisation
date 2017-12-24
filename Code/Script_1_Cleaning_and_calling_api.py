
# coding: utf-8

# In[1]:

import requests as req
import pytemperature
import time
APP_ID = 'get your api_key  from https://home.openweathermap.org/'


# In[2]:

#########################################################################################################################
##One Timer
# Importing csv file 
import pandas as pd
import numpy as np

df = pd.read_csv('ie-towns-sample.csv',header = None)

## Data Cleaning 
city_lat_lon_refined = []
cities = []
for index, row in df.iterrows():
    if row[3] not in cities:
        cities.append(row[3])
        city_lat_lon_refined.append([row[3],row[9],row[10]])


# In[4]:

#########################################################################################################################
# api call for data 
def api_call(lat='0',lon ='0'):
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+APP_ID
    url_data = req.get(url)
    return url_data.json()

data = api_call('2','3')
#temp_kelvin = data['main']['temp']
#temp_cel = pytemperature.k2c(temp_kelvin)
#pressure = data['main']['pressure']
#humidity = data['main']['humidity']
#wind_speed = data['wind']['speed']
#print(temp_cel,pressure,rain,wind_speed)
data


# In[4]:

def getting_data(lat='0',lon ='0'):
    data = api_call(lat,lon)
    temp_kelvin = data['main']['temp']
    temp_cel = pytemperature.k2c(temp_kelvin)
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    return temp_cel,pressure,humidity,wind_speed
#getting_data('4','7')


# In[5]:

#########################################################################################################################
# Api calls for multiple cities
def getting_info_for_one_time():
    inform_temp = []
    inform_pressure = []
    inform_humidity = []
    inform_wind_speed = []
    for city in city_lat_lon_refined:
        #print(data[1],data[2])
        lat = str(city[1])
        lon = str(city[2])
        temp,pressure,humidity,wind_speed = getting_data(lat,lon)
        inform_temp.append([city[0],city[1],city[2],temp])
        inform_pressure.append([city[0],city[1],city[2],pressure])
        inform_humidity.append([city[0],city[1],city[2],humidity])
        inform_wind_speed.append([city[0],city[1],city[2],wind_speed])
    return inform_temp,inform_pressure,inform_humidity,inform_wind_speed
#print(inform)
print(getting_info_for_one_time())


# In[ ]:

#########################################################################################################################
# appending data in CSV
import csv   
def append_info_in_csv(inform = [],file_name = 'Temprature.csv'):
    fields = []
    fields = [time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())]
    for info_row in inform:
        fields.append(info_row[3])
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

#append_info_in_csv()
#making_fields


# In[ ]:

#########################################################################################################################
# Collecting Data hourly
while True:
    #inform_temp,inform_pressure,inform_humidity,inform_wind_speed
    inform_temp,inform_pressure,inform_humidity,inform_wind_speed = getting_info_for_one_time()
    append_info_in_csv(inform_temp,'Temprature.csv')
    append_info_in_csv(inform_pressure,'Pressure.csv')
    append_info_in_csv(inform_humidity,'Humidity.csv')
    append_info_in_csv(inform_wind_speed,'Wind_Speed.csv')
    time.sleep(60)


# In[ ]:




# In[ ]:



