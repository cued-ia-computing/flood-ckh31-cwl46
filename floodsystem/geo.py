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


def rivers_by_station_number(stations, N):
    """Take the list of monitoring stations as MonitoringStation objects and
    an integer N. Return a list of tuples in form of (River Name, No. of Stations)
    of the N rivers with the greatest numbers of monitoring stations. The list is
    ordered in decreasing number of monitoring stations. All rivers with the same
    number of stations as the Nth river are included in the list.

    """

    stations_rivers = stations_by_river(stations)

    rivers_station_number = sorted_by_key([(river, len(stations_rivers[river])) for river in stations_rivers], 1, 1)

    stations_number = rivers_station_number[N - 1][1]

    return sorted_by_key([river_tuple for river_tuple in rivers_station_number if
                         river_tuple[1] >= stations_number], 1, True)


def stations_by_distance(stations, p):
    """Function the calculates distance from point p and sorts
    by distance from p """

    i = 0
    L = []

    for i in len(stations):
        from haversine import haversine, Unit
        distance = float(haversine(stations.coord,p))
        tup = (stations.name , distance)
        L.append(tup)
        L = sorted_by_key(L)
        return L 

def stations_within_radius(stations, centre, r):
    """Function to find all stations within a radius (r) of centre (centre)
    and sorts them alphabetically"""

    j = 0
    D = stations_by_distance(stations, centre)
    R = []
    N = []

    for j in len(stations):
        if stations.distance <= r:
            N = D[0]
            R.append(N)
        else:
            ""
        R = sorted(R)
        return R
