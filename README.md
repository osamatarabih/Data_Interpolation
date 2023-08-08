# Data_Interpolation
This Function interpolates time series data into Daily time series data. The Script includes two sub-scripts:   
1- Interp_PreProcess: This Script averages daily data if more than one measurement were recorded on this day, and it adds missing months (if any).   
2- A Spreadsheet (Days_Calc): This Spreadsheet determines the days and cumulative days per each observation.   
3- Interpolation: The main script which reads output from the previous two steps and the output is a daily interpolated time series of the observation time series.      **Data_Interpolations.py** is a standalone script that does the previous steps all-in-one to interpolate any type of weekly, bi-weekly, or monthly data to daily values. 
