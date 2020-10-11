# co2 data source: https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions
#  through:   https://github.com/owid/co2-data    (modified)

# temperature data source: https://www.statista.com/statistics/500472/annual-average-temperature-in-the-us/

import json
import matplotlib.pyplot as plot
import numpy as np

with open("/Users/oleksandr/Desktop/HW2/co2Data.json") as co2DataJason:
    co2Data = json.load(co2DataJason)["USA"]["data"]

with open("/Users/oleksandr/Desktop/HW2/temps.json") as tempDataJason:
    tempData = json.load(tempDataJason)

yearList= [] #same for both
co2List=[]
shareList=[]
tempList = []
for element in co2Data:
    yearList.append(element["year"])
    co2List.append(element["co2"] / 100)
    shareList.append(element["share_global_co2"])

for element in tempData:
    tempList.append(element["temp"])


fig, [ax1, ax2] = plot.subplots(2, figsize=(13, 10))


#first plot
x = np.arange(len(yearList))  # the label locations
width = 0.35  # the width of the bars
rects1 = ax1.bar(x - width/2, co2List, width, label='Production-based emissions of CO2 (hundred million tonnes)')
rects2 = ax1.bar(x + width/2, shareList, width, label='CO2 emissions as a percentage of the global total')
ax1.set(xlabel = 'Year')
adjustedYearsList = [0, 1990, 1995, 2000, 2005, 2010, 2015] # ax1.set_xticks(x) messed things up and i didnt know how to adjust
ax1.set_xticklabels(adjustedYearsList)
ax1.legend()
ax1.set_title('CO2 emmissions in the Untited States')


#second plot
ax2.set(xlabel = 'Year', ylabel = 'Temperature (Fahrenheit)')
ax2.plot(yearList, tempList, color='green', marker='o', linewidth=2, markersize=6)
ax2.set_title('Annual average temperatures in the United States')


plot.show()