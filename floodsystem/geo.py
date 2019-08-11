# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
from math import radians, cos, sin, asin, sqrt



def haversine(point1, point2, unit='km'):
    """ Calculate the great-circle distance between two points on the Earth surface.
    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.
    Keyword arguments:
    unit -- a string containing the initials of a unit of measurement (i.e. miles = mi)
            default 'km' (kilometers).
    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))
    :output: Returns the distance between the two points.
    The default returned unit is kilometers. The default unit can be changed by
    setting the unit parameter to a string containing the initials of the desired unit.
    Other available units are miles (mi), nautic miles (nmi), meters (m),
    feets (ft) and inches (in).
    """
    # mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
    AVG_EARTH_RADIUS_KM = 6371.0088

    # Units values taken from http://www.unitconversion.org/unit_converter/length.html
    conversions = {'km': 1,
                   'm': 1000,
                   'mi': 0.621371192,
                   'nmi': 0.539956803,
                   'ft': 3280.839895013,
                   'in': 39370.078740158}

    # get earth radius in required units
    avg_earth_radius = AVG_EARTH_RADIUS_KM * conversions[unit]

    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2

    return 2 * avg_earth_radius * asin(sqrt(d))

def stations_by_distance(stations, p):

    #Calculates distance from p to all stations, then orders them in order from
    #nearest station to furthest away
    
    #create empty list
    list_of_tuples = []
    for q in stations:
        
        #calculates distance of station from p
        distance = haversine(q.coord, p)
        
        #creates tuple with the name, town and distance (calculated above) of station
        tuple_of_station = (q.name, q.town, distance)
        
        #adds this tuple to the list
        list_of_tuples.append(tuple_of_station)
    
    return sorted_by_key(list_of_tuples, 2)


def rivers_with_station(stations):
    
    #creates an empty list of rivers with stations
    rivers = []
    
    #adds river to list if it is not already in the list
    for r in stations:
        river = r.river #sets variable as the river name
        #removes 'river' from the names
        if river.startswith('River'):
            rivers.append(river[:6])  #adds all of the string after 'River' '-space-' to the list
        else:
            rivers.append(river) 
    
    return set(rivers)

def stations_by_river(stations):
    #produces a dictionary where the river names are the key, and the stations on that river are the value
    
    river_with_stations = dict() #empty dictionary

    for i in stations:
        if i.river in river_with_stations: #if river is already a key in the dictionary 
            river_with_stations[i.river].append(i.name) #adds the name of the station to the list of values
        else:
            river_with_stations[i.river] = [i.name] #adds this river to the dictionary with the station name
    
    return (river_with_stations)



def stations_within_radius(stations, centre, r):
    list_stations=[] #produce an empty list
    for i in stations:
        distance = haversine(i.coord, centre) #find distances from stations to centre
        station_name = (i.name)
        if distance <= r:
            list_stations.append(station_name) #put names of stations that are in the circle in the list
    return list_stations        



def rivers_by_station_number(stations,N):
    stations_within_rivers = stations_by_river(stations) #dictiory which contains rivers as key and stations within each river as value
    station_numbers = {key: len(value) for key, value in stations_within_rivers.items()} #a new dictionary which convert lists of stations to numbers of stations
    value = sorted(station_numbers.items(), key=lambda x: x[1], reverse= True) #sort the new dictionary
    result = value[:N] #top n rivers in the dictionary
    while value[N-1][1]==value[N][1]:
        result.append(value[N]) #in case there is rivers with equal number of stations, also add those rivers to the list
        N+=1
    return result