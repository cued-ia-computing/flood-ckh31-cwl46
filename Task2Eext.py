# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels_ext, plot_water_levels_web


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    dt = 10
    p = 4

    # Identify stations with relative water level over threshold
    stations = stations_highest_rel_level(stations, 9)
    datess, levelss = [], []

    for station in stations[:9]:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        datess.append(dates)
        levelss.append(levels)

    plot_water_levels_web(stations[:9], datess, levelss, p)
    plot_water_levels_ext(stations[:6], datess[:6], levelss[:6], p)


if __name__ == "__main__":
    print("*** Task 2E extension: CUED Part IA Flood Warning System ***")
    run()
