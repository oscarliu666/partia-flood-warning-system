from floodsystem.geo import *
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher

# def test_river_names():
#     #this is a test that checks that the first item on the list of river names is 
#     #the same as the known first (alphabetically) item: 'Addlestone Bourne'

#     #set variable to the  list of the strings of names of rivers
#     river_names = list(rivers_with_station(stations= build_station_list()))

#     #checks that the first item on the list of river names is 'Addlestone Bourne'.
#     assert river_names[0] == 'Addlestone Bourne'

def test_rivers_with_stations():
    #This test checks that the length of the  list of rivers matches the known value of 471


    #builds list of stations
    stations = build_station_list()

    #runs the river function
    rivers = rivers_with_station(stations)

    #checks that the length of the list is correct
    assert len(rivers) == 471

test_rivers_with_stations()
# test_river_names()