# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 23:56:29 2018

@author: Ankit Goyal
"""

"""
Challenge Problem 1

"""
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as st
os.chdir("C:\Users\Ankit Goyal\Desktop\Udacity\Challenge")
# read the data 
df=pd.read_csv('Complaints.csv')
df_unique=df.drop_duplicates()
## This will drop row if any column as missing value
df_complete=df.dropna()
## we assume unique means when all column values are unique
df_new=df_complete.drop_duplicates()
print(df_new.info())
## to determine maximum complaint area we group by boroughs
df_group=df_new.groupby(['Borough of Occurrence'])
##this finds number of registered complaints by each boriugh
df_size=df_group.size()
#print(df_size.max())
#print(df_size.sum())
""" This is second answer"""
print(float(df_size.max())/df_size.sum())
## from wikipedia population of Brroklyn in 2016 is 2629150
per_100k=float(2629150)/100000
#print(per_100k)
df_2016=df_new[df_new['Incident Year']==2016]
df_2016=df_2016.groupby(['Borough of Occurrence'])
df_size_2016=df_2016.size()
#print(df_size_2016.max())
""" This is the third answer"""
print(float(df_size_2016.max())/per_100k)
df_new['average_time']=df_new['Close Year']-df_new['Received Year']
print(df_new['average_time'])
""" This is the 4th answer"""
print(sum(df_new['average_time']))/float(len(df_new['average_time']))
df_complaint=df_new[df_new['Allegation Description']=="Stop"]
df_complaint2=df_new[df_new['Allegation Description']=="Frisk"]
frames=[df_complaint,df_complaint2]
## getting the dataframe with allegations 'stop' or 'frisk'
final_data=pd.concat(frames)
## extracting data for years prior to 2016 including 2016
final_data_2016=final_data[(final_data['Incident Year']>=2008)& (final_data['Incident Year']<=2016)]
## Data from 2008 shows decline in trend

## groupby incident year
df_st_fr=final_data_2016.groupby(['Incident Year'])
print(df_st_fr.size())
df_incident_size=df_st_fr.size().to_frame('size')
df_incident_size['year']=df_incident_size.index
print(df_incident_size)
X=df_incident_size['year'].values
Y=df_incident_size['size'].values
X=np.reshape(X,(9,1))
Y=np.reshape(Y,(9,1))
model=LinearRegression()
model.fit(X,Y)
"""Answer to question 5 """
print(model.predict(2018))
df_new_chi=df_new[['Is Full Investigation','Complaint Has Video Evidence']]
chi=df_new_chi.groupby(['Is Full Investigation'])
chi_size=chi.size()
fal=pd.DataFrame(chi_size)
arr=fal.values
"""Answer to question 6 """
print(st.chisquare(arr))
df_uniq_2016=df_unique[df_unique['Incident Year']==2016]
## get total number of unique complaints with NA values
print(df_uniq_2016.info())
## calculating proportionality factor Officer/complaints (below is just FYI, not required for calculations)
propfac=float(36000)/7878
df_2016_v2=df_uniq_2016.groupby(['Borough of Occurrence'])['UniqueComplaintId']
df_2016_v2=pd.DataFrame(df_2016_v2.size())
complaints=df_2016_v2.values
#complaints.reshape(1,6)
arr1=['Bronx','Brooklyn','Manhattan','Outside NYC','Queens','Staten Island']
## number of precinct in each borrough
arr2=np.array([12,23,22,0,16,4])
arr2=arr2.reshape(6,1)
complaints=(complaints.reshape(6,1))
## calculates number of complaints per precinct for each borough and store in arr3, values in this array can be used to 
## calculate desired proportion as number of officers are proportional to number of complaints.
arr3=np.array((complaints.astype(float))/arr2.astype(float))
print(arr3[0]/arr3[2])