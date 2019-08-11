from floodsystem.plot import plot_water_levels
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem import datafetcher
from floodsystem.station import MonitoringStation

def takeSecond(elem):
    return elem[1] #function to assist in sorting by second element of tuple

stations = build_station_list()
update_water_levels(stations)


for i in stations:
    if i.typical_range_consistent() == True:
        i.relative_water_level()    #sets up relative level values for the stations taht have consistent typical range

station_with_levels = []

for x in stations:
    if x.relative_level is not None:
        station_with_levels.append((x, x.relative_level, x.typical_range))


sorted_list = sorted(station_with_levels, key=takeSecond, reverse = True)

final_list = sorted_list[:5]

#tests
for i in final_list:
    station = i[0]
    assert station.relative_level is not None

#produces the plots  
for i in final_list:
    plot_water_levels(i[0], 10, i[2])


# plot_water_levels(i[0], 10, i[2])
# stroud_stations = []
# for i in stations:
#     if i.latest_level is not None:
#         if i.typical_range is not None:
#             i.relative_water_level()
#             if i.name == 'Chalford':
#                 stroud_stations.append((i, i.relative_level, i.typical_range))

# station_to_plot = stroud_stations[0]   
# plot_water_levels(station_to_plot[0], 10, station_to_plot[2])

        