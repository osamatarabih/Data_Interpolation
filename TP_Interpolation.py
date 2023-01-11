# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:14:29 2020

@author: osama
"""
import pandas as pd
import numpy as np
from datetime import date
#Interpolate TSS data to get daily TSS values.
L004_TSS_In = pd.read_csv('C:/Work/Research/LOONE/Nitrogen Module/Module_Inputs/L008_Temperature_No_Months_Missing.csv')
#Remove Negative Data Values
L004_TSS_In = L004_TSS_In[L004_TSS_In['Data'] >= 0]
L004_TSS_In['Date'] = pd.to_datetime(L004_TSS_In['Date'], format = '%Y-%m-%d')
L004_TSS_start_date = L004_TSS_In['Date'].iloc[0]
L004_TSS_end_date = L004_TSS_In['Date'].iloc[-1]
date_rng_TSS_1 = pd.date_range(start=L004_TSS_start_date, end = L004_TSS_end_date, freq= 'D')
#Create a data frame with a date column
L004_TSS_df = pd.DataFrame(date_rng_TSS_1, columns =['Date'])
L004_TSS_len = len(L004_TSS_df.index)
L004_TSS_Cum_days = np.zeros(L004_TSS_len)
L004_TSS_daily = np.zeros(L004_TSS_len)
#Set initial values
L004_TSS_Cum_days[0] = L004_TSS_df['Date'].iloc[0].day
L004_TSS_daily[0] = L004_TSS_In['Data'].iloc[0]
for i in range (1,L004_TSS_len):
    L004_TSS_Cum_days[i] = L004_TSS_Cum_days[i-1]+1
    #L004_TSS_daily[i] = interpolate.interp1d(L004_TSS_In['Days'],L004_TSS_In['TSS'] , kind = 'linear')(L004_TSS_Cum_days[i])
    L004_TSS_daily[i] = np.interp(L004_TSS_Cum_days[i], L004_TSS_In['Days_cum'], L004_TSS_In['Data'])
L004_TSS_df['Data'] = L004_TSS_daily
L004_TSS_df.to_csv('C:/Work/Research/LOONE/Nitrogen Module/Module_Inputs/L008_Temperature_Interpolated.csv')
