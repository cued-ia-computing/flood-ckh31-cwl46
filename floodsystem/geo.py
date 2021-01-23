# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


def rivers_with_station(stations):
    """Take the list of monitoring stations as MonitoringStation objects.
    Return a set of all rivers with at least one monitoring station. Rivers
    are arranged in alphabetical order.

    """

    rivers = set(station.river for station in stations if station.river is not None)

    return sorted(rivers)


def stations_by_river(stations):
    """Take the list of monitoring stations as MonitoringStation objects.
    Return a dictionary which maps rivers as keys to a list of MonitoringStation
    objects on a given river.

    """

    rivers = rivers_with_station(stations)
    stations_rivers = {river: [] for river in rivers}

    for station in stations:
        stations_rivers[station.river].append(station)

    return stations_rivers
