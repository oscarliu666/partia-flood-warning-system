from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
import datetime
def run():
    stations = build_station_list()
    update_water_levels(stations)#Update water levels

    list_of_top_stations = stations_highest_rel_level(stations,5)#Find a list of five stations with largest relative heights
    list_of_information = [] #Create an empty list
    for i in list_of_top_stations:
        for j in stations:
            if i[0]==j.name:
                list_of_information.append(j) #Add top 5 stations with full information to the list
    
    for x in list_of_information:
        dt = 2 #For last two days
        dates, levels = fetch_measure_levels(x.measure_id,dt=datetime.timedelta(days=dt)) #Create a tuple with time and height
        plot_water_level_with_fit(x,dates,levels,4) #plot graphs
    return

run()



