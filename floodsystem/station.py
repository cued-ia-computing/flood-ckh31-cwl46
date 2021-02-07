# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

from datetime import date


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 extreme_values, river, town, catchment, date_open):

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._extreme_values = extreme_values
        self._river = river
        self._town = town
        self._catchment = catchment
        self._date_open = date_open

        self._latest_level = None

    def typical_range_consistent(self):

        P = True

        if self.typical_range is None:
            P = False
        else:
            lower = self.typical_range[0]
            higher = self.typical_range[1]
            if higher < lower:
                P = False
            else:
                P = True
        return P

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
    def extreme_values(self):
        return self._extreme_values

    @property
    def river(self):
        return self._river

    @property
    def town(self):
        return self._town

    @property
    def catchment(self):
        return self._catchment

    @property
    def date_open(self):
        return self._date_open

    @property
    def latest_level(self):
        return self._latest_level

    @latest_level.setter
    def latest_level(self, latest_level):
        self._latest_level = latest_level
        return True

    def __repr__(self):
        d = "Station name:      {}\n".format(self.name)
        d += "   id:             {}\n".format(self.station_id)
        d += "   measure id:     {}\n".format(self.measure_id)
        d += "   coordinate:     {}\n".format(self.coord)
        d += "   town:           {}\n".format(self.town)
        d += "   river:          {}\n".format(self.river)
        d += "   catchment:      {}\n".format(self.catchment)
        d += "   extreme values: {}\n".format(self.extreme_values)
        d += "   opening date:   {}\n".format(date.isoformat(self.date_open))
        d += "   typical range:  {}".format(self.typical_range)
        return d


def inconsistent_typical_range_stations(stations):

    ListF = [station.typical_range_consistent() for station in stations]
    i = 0
    Names = []

    while i < len(ListF):
        if ListF[i] is False:
            Names.append(stations[i])
        else:
            ""
        i += 1

    return Names
