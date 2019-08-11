from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_level_over_threshold
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
import numpy as np
import datetime
import matplotlib.pyplot as plt
from floodsystem.analysis import polyfit

def stations_level_over_threshold_without_test(stations, tol):
	stations_tuple_with_relative = []
	for i in stations:
		if i.typical_range_consistent() == True:
			i.relative_water_level() 
			if i.relative_level is not None:
				if i.relative_level > tol:
					stations_tuple_with_relative.append((i.name, i.relative_level))
	return stations_tuple_with_relative#Give a list with relative heights with names

def typical_range_consistent1(stations):
	#checks whether the typical high or low range is consistent

	if stations.typical_range is None: #finds if there is data available
		return False
	if stations.typical_range[0] > stations.typical_range[1]: #finds if the high value < low value
		return False
	return True #if these requirements are not met, the data is consistent#Get rid of stations with inconsistant range

def run():
	stations=[]#Create a new list
	list_2 = []#Create a new list
	full = build_station_list()
	update_water_levels(full)#Update water level information
	list_1=stations_highest_rel_level(full, 5)#Only top 100 due to large calculation for full lists and 100 is probably enough for risk prediction

	for i in list_1:
		for j in full:
			if i[0]==j.name:
				list_2.append(j) #Add top 100 stations with full information to a list
	
	for i in list_2:
		if i.latest_level is None:#Get rid of those with no latest level informaiton
			continue
		else:
			stations.append(i)#List of stations with full information and high relative heights

	list_of_name=[]

	for j in stations:
		list_of_name.append(j.name) #Collect valid stations' name

	listofzeros = [0]*(len(list_of_name))

	original_risk_value = dict( zip(list_of_name,listofzeros )) #Produce a dictionary for all stations with risk value of 0

	list_of_relative = stations_level_over_threshold_without_test(stations = stations, tol = 0)#Give a list with relative heights with names

	for i in list_of_relative:
		if i[1]>=0.8:#if relative height greater than 0.8, plus 3 risk value
			original_risk_value.update({i[0]: 3})
		if 0.8>i[1]>=0.7:#between 0.8-0.7, plus 2 risk value
			original_risk_value.update({i[0]: 2})
		if 0.7>i[1]>=0.3:#between 0.7-0.3, plus 1 risk value
			original_risk_value.update({i[0]: 1})
		if i[1]<0.3:#under 0.3, plus 0 risk value
			original_risk_value.update({i[0]: 0})


	for x in stations:
		dt = 2
		dates1, levels1 = fetch_measure_levels(x.measure_id,dt=datetime.timedelta(days=dt))#obtain levels against time data
		if len(dates1) == 0: #Git rid of those with missing date
			continue
		if len(levels1) == 0:#Get rid of those with missing levles
			continue	
		else:
			poly,shift = polyfit(dates1,levels1,4)#Get functions of best fit from above information
			height = poly(-1)#Predict height for tomorrow
			a = height-x.typical_range[0]    #calculates current level above lowest level
			b = x.typical_range[1] - x.typical_range[0]   #calculates value of range of lowest to highest level
			relative = (a/b)#Calculate relative height for tomorrow
			if relative>=0.8:#if relative height greater than 0.8, plus 3 risk value
				original_risk_value.update({x.name: 3 + original_risk_value[x.name]})
			if 0.8>relative>=0.7:#between 0.8-0.7, plus 2 risk value
				original_risk_value.update({x.name: 2 + original_risk_value[x.name]})
			if 0.7>relative>=0.3:#between 0.7-0.3, plus 1 risk value
				original_risk_value.update({x.name: 1 + original_risk_value[x.name]})
			if relative<0.3:#under 0.3, plus 0 risk value
				original_risk_value.update({x.name: 0 + original_risk_value[x.name]})

	severe=[]
	high=[]
	moderate=[]
	low=[]
	for i in list_of_name:
		x=original_risk_value[i]
		if x>=6:#risk value of 6 is classified as severe
			severe.append(i)
		if 5>=x>4:#risk value of of 5 is classified as high
			high.append(i)
		if 4>=x>2:#risk value of 4 and 3 is classified as moderate
			moderate.append(i)
		if x<=2:#risk value of 2,1,0 is classified as low
			low.append(i)



	print("severe staions",severe)
	print("high staions",high)
	print("moderate staions",moderate)
	print("low staions",low)

run()