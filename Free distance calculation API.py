#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import requests

df=pd.read_excel('Your path')
df['Current Geographical distance']=""
df['Current Geographical duration']=""
df.head()

for i in range(0,len(df)):
    a =requests.get("https://api.neshan.org/v1/distance-matrix?origins="+str(df.loc[i,'Lat'])+","+str(df.loc[i,'Long'])+"&destinations="+str(df.loc[i,'Lat Current location'])+","+str(df.loc[i,'Long Current location']),headers={"Api-Key": "INSERT YOUR SERVICE CODE FROM Neshan.ir WEBSITE"}).json()
    if "rows" in a:
#        print(a)
        df.loc[i,'Current Geographical distance']=a['rows'][0]['elements'][0]['distance']['value']
        df.loc[i,'Current Geographical duration']=(a['rows'][0]['elements'][0]['duration']['value'])/60
    else:
#        print("Nothing")
        df.loc[i,'Current Geographical distance']=""
        df.loc[i,'Current Geographical duration']=""


df.to_excel('Your path')
