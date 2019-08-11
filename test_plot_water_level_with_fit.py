from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_level_with_fit
import datetime
import matplotlib.pyplot as plt
import matplotlib
def run():
    stations = build_station_list()
    update_water_levels(stations)
    key =stations[0].measure_id
    station = stations[0]
    dt = 5
    dates, levels = fetch_measure_levels(key,dt=datetime.timedelta(days=dt))
    p=4
    plot_water_level_with_fit(station,dates,levels,p)
run()
    