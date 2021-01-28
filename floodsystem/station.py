# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._river = river
        self._town = town

        self._latest_level = None

    def typical_range_consistent(self):

        P = True
        TFList = []

        if self._typical_range is None:
            P = False
            tup = (self.name, P)
            TFList.append(tup)
        elif self._typical_range < 0:
            P = False
            tup = (self.name, P)
            TFList.append(tup)
        else:
            P = True
            tup = (self.name, P)
            TFList.append(tup)
        return TFList

    @property
    def station_id(self):
        return self._station_id

    @property
    def measure_id(self):
        return self._measure_id

    @property
    def name(self):
        return self._name

    @property
    def coord(self):
        return self._coord

    @property
    def typical_range(self):
        return self._typical_range

    @property
    def river(self):
        return self._river

    @property
    def town(self):
        return self._town

    @property
    def latest_level(self):
        return self._latest_level

    @latest_level.setter
    def latest_level(self, latest_level):
        self._latest_level = latest_level
        return True

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d


def inconsistent_typical_range_stations(stations):

    ListF = MonitoringStation.typical_range_consistent(stations)
    i = 0
    Q = []

    while i < len(ListF):
        F = ListF[i]
        P = F[1]
        if P is False:
            Q.append(F)
        else:
            ""
        i += 1
    return Q
