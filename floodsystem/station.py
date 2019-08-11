# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""
from . import stationdata

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        self.relative_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        #checks whether the typical high or low range is consistent

        if self.typical_range is None: #finds if there is data available
            return False
        if self.typical_range[0] > self.typical_range[1]: #finds if the high value < low value
            return False
        return True #if these requirements are not met, the data is consistent

    def relative_water_level(self):
        #returns the relative water level to typical range where 0.0 is lowest level and 1.0 is highest, 
        #but returns 'None' if the data in unnavailable
        

        #checks whether data is available 
        if self.latest_level is not None:
            a = self.latest_level - self.typical_range[0]    #calculates current level above lowest level
            b = self.typical_range[1] - self.typical_range[0]   #calculates value of range of lowest to highest level
            # assert a < b 
            # assert b > 0    #checks that the values are reasonable
            if a < b:
                if a/b > 0.0:            ###new*|****|
                    self.relative_level = a/b    #calculates relative value
                    assert self.relative_level is not None 
                    return (self.relative_level)
        elif self.latest_level is None:  #returns None if there is no value
            self.relative_level = None
            # return (self.relative_level)
            

def inconsistent_typical_range_stations(stations):
    #runs the typical_range_consistent function and produces a list of
    #stations with inconsistent typical range

    inconsistent_stations = []
    
    for i in stations:
        if i.typical_range_consistent() == False: #if the data is consistent
            inconsistent_stations.append(i.name) #add to the list

    return(inconsistent_stations)

