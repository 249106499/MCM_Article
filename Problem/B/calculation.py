import pandas as pd
from pandas import *
from scipy import optimize
from math import radians, cos, sin, asin, sqrt
import numpy as np
import pylab as py
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import itertools

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def getLon(text):
    return str.split(text)[0]

def getLat(text):
    return str.split(text)[0]

order_filename = "Appendix-1.xls"
usr_filename = "Appendix-2.xlsx"

order = pd.read_excel(order_filename)
user = pd.read_excel(usr_filename)
order = order.rename(index=str,columns={"任务gps 纬度":"GPS_Lat","任务gps经度":"GPS_Lon"})
user["GPS_Lon"]=pd.to_numeric(user["会员位置(GPS)"].apply(lambda x:str.split(x)[0]))
user["GPS_Lat"]=pd.to_numeric(user["会员位置(GPS)"].apply(lambda x:str.split(x)[1]))

order_user = DataFrame(columns=["order","user"])

distance = np.empty([order.__len__(),user.__len__()])
for i in range(0,order.__len__()):
    lon = order.ix[i]["GPS_Lon"]
    lat = order.ix[i]["GPS_Lat"]
    if(i%100==0):
        print(i)
    for j in range(0,user.__len__()):
        distance[i][j]=haversine(lon,lat,user.ix[j]["GPS_Lon"],user.ix[j]["GPS_Lat"])



for i in range(0,order.__len__()):
    for j in range(0,user.__len__()):
        print(order.ix[i]["GPS_Lon"],order.ix[i]["GPS_Lat"])
        print(user.ix[j]["GPS_Lon"],user.ix[j]["GPS_Lat"])
        print(distance[i][j])
        input()

