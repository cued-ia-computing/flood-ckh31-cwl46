"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import (rivers_with_station, stations_by_river, rivers_by_station_number,
                             stations_by_distance, stations_within_radius)


def test_rivers_with_station():

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_with_station(stations)

    assert type(rivers) == list


def test_stations_by_river():

    # Build list of stations
    stations = build_station_list()

    stations_rivers = stations_by_river(stations)

    assert type(stations_rivers) == dict
    for station in stations:
        assert station.river in stations_rivers.keys()


def test_rivers_by_station_number():

    # Build list of stations
    stations = build_station_list()

    rivers = rivers_by_station_number(stations, 20)

    assert type(rivers) == list
    assert all(type(river) == tuple for river in rivers)
    assert len(rivers) >= 20


def test_stations_by_distance():

    # Build list of stations
    stations = build_station_list()

    stations = stations_by_distance(stations, [0, 0])

    assert type(stations) == list
    assert all(type(station) == tuple for station in stations)
    assert all(type(station[0]) == str for station in stations)
    assert all(type(station[1]) == float for station in stations)
    assert all(stations[i][1] < stations[i + 1][1] for i in range(len(stations) - 1))


def test_stations_within_radius():

    # Build list of stations
    stations = build_station_list()

    stations = stations_within_radius(stations, (52.2053, 0.1218), 20)

    assert type(stations) == list
    assert all(type(station) == str for station in stations)
