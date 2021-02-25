
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
import numpy


def test_polyfit():

    # Build list of stations
    stations = build_station_list()
    dt = 10
    p = 4
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, p)

    assert type(poly) == numpy.poly1d
    assert type(d0) == datetime.datetime
    assert d0 == dates[-1]
