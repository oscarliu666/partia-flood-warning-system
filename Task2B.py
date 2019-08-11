from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem import datafetcher
from floodsystem.station import MonitoringStation
from floodsystem.flood import takeSecond
from floodsystem.flood import stations_level_over_threshold


stations = build_station_list()

update_water_levels(stations)  #updates the water levels so that a relative level can be calculated

relative_levels = []

# for i in stations:
#     if i.typical_range_consistent() == True:  #checks that the typical ranges are consistent
#         i.relative_water_level()
#         a = i.relative_level     #assigns variable
#         if a is not None:   #checks there is a value
#             if a > 0.8:
#                 print(i.name, i.relative_level)

list_tuples = stations_level_over_threshold(stations = stations, tol = 0.8)
print(list_tuples)