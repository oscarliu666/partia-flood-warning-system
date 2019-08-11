from fake_directory import *
from floodsystem.geo import *

def test_station_distances():
    
    #creates empty tuple
    station_with_distance = ()
    
    stations = []
    stations = build_station_list()

    # selects nearest station to Cam
    station_with_distance = stations_by_distance(stations, (52.2053, 0.1218))[0]
    
    #sets variable as the value of distance of this station from Cam
    computed_distance = station_with_distance[-1]
    rounded_distance = round(computed_distance, 2)
    
    # Assert that station is distance 0.84
    assert rounded_distance == 0.84

test_station_distances()
