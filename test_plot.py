
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels, plot_water_levels_ext, plot_water_levels_web, plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def test_plot_water_levels():

    # Build list of stations
    stations = build_station_list()
    dt = 10

    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(station, dates, levels)


def test_plot_water_levels_ext():

    # Build list of stations
    stations = build_station_list()
    dt = 10
    p = 4

    stations = stations[:6]
    datess, levelss = [], []
    for station in stations[:6]:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        datess.append(dates)
        levelss.append(levels)

    plot_water_levels_ext(stations[:6], datess, levelss, p)


def test_plot_water_levels_web():

    # Build list of stations
    stations = build_station_list()
    dt = 10
    p = 4

    stations = stations[:9]
    datess, levelss = [], []
    for station in stations[:9]:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        datess.append(dates)
        levelss.append(levels)

    plot_water_levels_web(stations[:9], datess, levelss, p)


def test_plot_water_level_with_fit():

    # Build list of stations
    stations = build_station_list()
    dt = 10
    p = 4

    station = stations[0]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(station, dates, levels, p)
