from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit
import datetime
import numpy as np


def run():

    stations = build_station_list()
    update_water_levels(stations)
    key =stations[1].measure_id
    dt = 2
    dates, levels = fetch_measure_levels(key,dt=datetime.timedelta(days=dt))
    poly,shift = polyfit(dates,levels,4)
    print(poly)
    print(shift) 

run()


