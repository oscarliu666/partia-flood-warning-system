from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
import Task1C
import pytest

def test_station_within_radius():
    list_distance=stations_by_distance(build_station_list(),(52.2053, 0.1218)) #list of distances from stations to cambridge
    sample = list_distance[:5]
    distance = (sample[3][2]+0.1) #distance to the fourth closest station
    result = stations_within_radius(build_station_list(),(52.2053, 0.1218),distance) #number of stations within that distance
    assert len(result) == 4 #Test if there are four stations
    
test_station_within_radius()