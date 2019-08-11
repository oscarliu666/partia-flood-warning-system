from floodsystem.geo import *
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher

#build station list
stations = build_station_list()

def run():
   
    print (stations_by_distance(build_station_list(), (52.2053, 0.1218))[:9]) #prints nearest 10
    print (stations_by_distance(build_station_list(), (52.2053, 0.1218))[-10:]) #prints furthest 10


# def run():
   
#     print (stations_by_distance(build_station_list(), (51.753282, -2.139221))[:9]) #prints nearest 10
#     # print (stations_by_distance(build_station_list(), (52.2053, 0.1218))[-10:]) #prints furthest 10

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

# rivers = rivers_with_station(stations= build_station_list())
# print(rivers)