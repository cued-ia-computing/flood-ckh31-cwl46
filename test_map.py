"""Unit test for the map module"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.map import location_map, location_rel_level_map


def test_location_map():

    # Build list of stations
    stations = build_station_list()

    location_map(stations)


def test_location_rel_level_map():

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    location_rel_level_map(stations)
