"""Unit test for the map module"""

from floodsystem.stationdata import build_station_list
from floodsystem.map import location_map


def test_location_map():

    # Build list of stations
    stations = build_station_list()

    location_map(stations)
