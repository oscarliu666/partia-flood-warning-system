from floodsystem.geo import *
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher
from floodsystem.station import *

stations_with_inconsistent_typical_range = inconsistent_typical_range_stations(stations=build_station_list()) 
stations_with_inconsistent_typical_range = sorted(stations_with_inconsistent_typical_range)
print(stations_with_inconsistent_typical_range)


