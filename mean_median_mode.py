import pandas as pd
import math
import statistics

data = pd.read_csv('./C-104_data.csv')
data_array = data["Weight(Pounds)"].values
sum = 0
for i in range(0,len(data_array)):
    sum = sum + data_array[i]
    i+=1
mean = sum/len(data_array)
print("Mean of the data ------> ",mean)
data_array.sort()
medianPos = round(len(data_array)/2)
median = data_array[medianPos]
print("Median of the data ----> ",median)
mode = statistics.mode(data_array)
print("Mode of the data ------> ",mode)