
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level


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
