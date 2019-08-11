from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem import datafetcher
from floodsystem.flood import stations_highest_rel_level
stations = build_station_list()
update_water_levels(stations)
print(stations_highest_rel_level(stations,10))








