# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation1:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        
        self.station_id = 'abc123'
        self.measure_id = 'abc123'
        self.name = 'myhouse'
        self.coord = (52.2054, 0.1219)  #one unit off being p
        self.typical_range = 2, 1 #clearly wrong
        self.river = 'River Cam' #
        self.town = 'Cambridge'
        self.latest_level = None

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

        if self.typical_range is None: #checks that there is data available
            return False
        if self.typical_range[0] > self.typical_range[1]: #checks that the high value > low value
            return False
        return True #if these requirements are not met, the data is consistent


    # Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides interface for extracting statiob data from
JSON objects fetched from the Internet and

"""

from floodsystem import datafetcher




def build_station_list(use_cache=True):
    """Build and return a list of all river level monitoring stations
    based on data fetched from the Environment agency. Each station is
    represented as a MonitoringStation object.

    The available data for some station is incomplete or not
    available.

    """

    # Fetch station data
    data = datafetcher.fetch_station_data(use_cache)

    # Build list of MonitoringStation objects
    stations = []
    for e in data["items"]:
        # Extract town string (not always available)
        town = None
        if 'town' in e:
            town = e['town']

        # Extract river name (not always available)
        river = None
        if 'riverName' in e:
            river = e['riverName']

        # Attempt to extract typical range (low, high)
        try:
            typical_range = (float(e['stageScale']['typicalRangeLow']),
                             float(e['stageScale']['typicalRangeHigh']))
        except Exception:
            typical_range = None

        try:
            # Create mesure station object if all required data is
            # available, and add to list
            s = MonitoringStation1(
                station_id=e['@id'],
                measure_id=e['measures'][-1]['@id'],
                label=e['label'],
                coord=(float(e['lat']), float(e['long'])),
                typical_range=typical_range,
                river=river,
                town=town)
            stations.append(s)
        except Exception:
            # Not all required data on the station was available, so
            # skip over
            pass

    return stations

