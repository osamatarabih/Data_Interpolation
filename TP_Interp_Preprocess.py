# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:09:49 2021

@author: osama
"""

#This Script prepares nutrient data for interpolation process!

#First, import required Packages
import pandas as pd
import numpy as np
import datetime
#Read Nutrient Data after pre-processing! (Only Samples, No Negative Values)
L007_TSS = pd.read_csv('C:/Work/Research/LOONE/Nitrogen Module/Module_Inputs/L008_Temperature.csv')
L007_TSS = L007_TSS.set_index(['Date'])
L007_TSS.index = pd.to_datetime(L007_TSS.index, unit = 'ns')
L007_TSS_df = L007_TSS.resample('D').mean()
L007_TSS_df = L007_TSS_df.dropna(subset = ['Temperature_Deg C'])
L007_TSS_df = L007_TSS_df.reset_index()
L007_TSS_df['Yr_M'] = pd.to_datetime(L007_TSS_df['Date']).dt.to_period('M')
start_date = L007_TSS_df['Date'].iloc[0]
end_date = L007_TSS_df['Date'].iloc[-1]
date_rng = pd.date_range(start = start_date, end = end_date, freq = 'M')
Monthly_df = pd.DataFrame(date_rng, columns=['Date'])
Monthly_df['Yr_M'] = pd.to_datetime(Monthly_df['Date']).dt.to_period('M')
New_date = []
New_data = []
#Set index for the two dataframes 
L007_TSS_df = L007_TSS_df.set_index(['Yr_M'])
Monthly_df = Monthly_df.set_index(['Yr_M'])
for i in Monthly_df.index:
    if i in L007_TSS_df.index:
        if type(L007_TSS_df.loc[i]['Date']) == pd.Timestamp:
            New_date.append(L007_TSS_df.loc[i]['Date'])
            New_data.append(L007_TSS_df.loc[i]['Temperature_Deg C'])
        else:
            for j in range(len(L007_TSS_df.loc[i]['Date'])):
                New_date.append(L007_TSS_df.loc[i]['Date'][j])
                New_data.append(L007_TSS_df.loc[i]['Temperature_Deg C'][j])
    elif i not in L007_TSS_df.index:
        New_date.append(datetime.datetime(Monthly_df.loc[i]['Date'].year,Monthly_df.loc[i]['Date'].month,1))
        New_data.append(np.NaN)
Final_df = pd.DataFrame()
Final_df['Date'] = New_date
Final_df['Data'] = New_data
Final_df.to_csv('C:/Work/Research/LOONE/Nitrogen Module/Module_Inputs/L008_Temperature_No_Months_Missing.csv')

