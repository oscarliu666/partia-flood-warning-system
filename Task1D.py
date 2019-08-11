from floodsystem.geo import *
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher

rivers = rivers_with_station(stations = build_station_list())  #runs the function with all of the stations
rivers_sorted = sorted(rivers) #sorts the set
# print(rivers_sorted) 
# rivers_sorted_list = list(rivers_sorted)

# j = 0
# for i in rivers_sorted_list:
#     print(j, i)
#     j += 1



station_dictionary = stations_by_river(stations = build_station_list())
# print(station_dictionary)
# length = len(station_dictionary)
# print(length)


print('Number of Rivers with at least one Station on is:', len(rivers_sorted))


print(rivers_sorted[0:10])

list_of_rivers = ['River Aire', 'River Cam', 'River Thames'] 
for i in list_of_rivers:
    list_stations = station_dictionary.get(i) #for each river get the
    list_stations_sorted = sorted(list_stations) #sorts the list into alphabetical order
    print(i, list_stations_sorted)


# print(station_dictionary.get('River Aire'))
