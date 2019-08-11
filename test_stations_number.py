from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
import Task1E
import pytest
def test_rivers_by_station_number():
    stations = build_station_list()
    name = rivers_by_station_number(stations,12)[0][0] #Name of the river with largest number of stations
    number = len(rivers_by_station_number(stations,12)) #Top 13 rivers will include rivers with same number of stations
    assert name =="River Thames"   #Correct river is presented
    assert number > 13 #Rivers with same number of stations are included as there are more than 13 rivers in the list

test_rivers_by_station_number()