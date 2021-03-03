
from floodsystem.analysis import polyfit, prediction
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


def test_prediction():

    # Build list of stations
    stations = build_station_list()
    dt = 10
    p = 4
    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d0 = polyfit(dates, levels, p)
    forecast = prediction(poly, dates, d0)

    assert type(forecast) == numpy.ndarray
    assert len(forecast) == 6
    assert all(type(value) == numpy.float64 for value in forecast)
