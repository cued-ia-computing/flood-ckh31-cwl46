"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


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
