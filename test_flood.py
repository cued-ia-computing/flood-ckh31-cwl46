
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import (stations_level_over_threshold, stations_highest_rel_level,
                               update_stations_risk, update_flood_warnings)


def test_stations_level_over_threshold():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    stations_tuple = stations_level_over_threshold(stations, 0.5)

    assert type(stations_tuple) == list
    assert all(type(item) == tuple for item in stations_tuple)
    assert all(type(item[0]) == MonitoringStation for item in stations_tuple)
    assert all(type(item[1]) == float for item in stations_tuple)
    assert all(item[1] > 0.5 for item in stations_tuple)
    assert all(stations_tuple[i][1] >= stations_tuple[i + 1][1] for i in range(len(stations_tuple) - 1))


def test_stations_highest_rel_level():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    stations = stations_highest_rel_level(stations, 15)

    assert type(stations) == list
    assert len(stations) == 15
    assert all(type(item) == MonitoringStation for item in stations)
    assert all(stations[i].relative_water_level() >= stations[i + 1].relative_water_level()
               for i in range(len(stations) - 1))


def test_update_stations_risk():
    # Build list of stations
    stations = build_station_list()[:10]
    update_water_levels(stations)
    station = stations[0]
    station.latest_level = None
    stations.append(station)
    stations_return = update_stations_risk(stations)

    assert any(station.risk_index is not None for station in stations)
    assert type(stations_return) == list
    assert len(stations_return) == 11
    assert all(type(ret) == tuple for ret in stations_return)
    assert all(type(ret[0]) == MonitoringStation for ret in stations_return)
    assert all(type(ret[1]) == int or ret[1] is None for ret in stations_return)
    assert all(ret[1] >= 0 and ret[1] <= 7 for ret in stations_return if ret[1] is not None)


def test_update_flood_warnings():
    # Build list of stations
    stations = build_station_list()[:10]
    update_water_levels(stations)

    # Create multiple stations in the same town
    stations.append(stations[0])

    # Create all possible values of risk_index
    stations[2].risk_index = 0
    stations[3].risk_index = 1
    stations[4].risk_index = 2
    stations[5].risk_index = 3
    stations[6].risk_index = 4
    stations[7].risk_index = 5
    stations[8].risk_index = 6
    stations[9].risk_index = 7

    towns = update_flood_warnings(stations)

    assert type(towns) == dict
    assert all(station.town in towns for station in stations)
    assert all(towns[town] is None or towns[town] in ["severe", "high", "moderate", "low"] for town in towns)
