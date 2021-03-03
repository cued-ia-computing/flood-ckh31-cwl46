
from .utils import sorted_by_key
from .datafetcher import fetch_measure_levels
from .analysis import polyfit, prediction
import datetime


def stations_level_over_threshold(stations, tol):

    F = []
    r = [station.relative_water_level() for station in stations]
    i = 0

    for station in stations:
        if r[i] is not None:
            q = (station, r[i])
            if r[i] > tol:
                F.append(q)
        i += 1

    F = sorted_by_key(F, 1, True)
    return F


def stations_highest_rel_level(stations, N):

    r = [station.relative_water_level() for station in stations]
    S = []
    i = 0

    for station in stations:
        if r[i] is not None:
            q = (station, r[i])
            S.append(q)
        i += 1

    S = sorted_by_key(S, 1, True)
    return [s[0] for s in S[:N]]


def update_station_risk(station):
    """Take a MonitoringStation object. Set its risk index.
    Return a tuple of (MonitoringStation object, risk_index).

    """

    if station.relative_water_level() is not None:
        dt = 2
        p = 4

        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

        if dates != [] and levels != []:
            poly, d0 = polyfit(dates, levels, p)
            forecast_levels = prediction(poly, dates, d0)

            def relative_water_level(station, level):
                return (level - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])

            relative_levels = [relative_water_level(station, forecast_level) for forecast_level in forecast_levels]
            relative_levels.append(station.relative_water_level())

            risk_index = 0
            for relative_level in relative_levels:
                if relative_level > 0.8:
                    risk_index += 1

            station.risk_index = risk_index
            return (station, risk_index)

    station.risk_index = None
    return (station, None)


def update_stations_risk(stations):
    """Take a list of MonitoringStation objects. Set their risk indices.
    Return a list of tuples of (MonitoringStation object, risk_index).

    """

    return [update_station_risk(station) for station in stations]


def update_flood_warnings(stations):
    towns = {}
    warning_levels = {}
    for station in stations:
        if station.town is not None:
            if station.town in towns:
                towns[station.town].append(station)
            else:
                towns[station.town] = [station]

    for town in towns:
        cumulative_index = 0
        count = 0
        for station in towns[town]:
            if station.risk_index is not None:
                cumulative_index += station.risk_index
                count += 1
        if count != 0:
            average_index = cumulative_index / count

            if average_index >= 6:
                warning_levels[town] = "severe"
            elif average_index >= 4:
                warning_levels[town] = "high"
            elif average_index >= 2:
                warning_levels[town] = "moderate"
            else:
                warning_levels[town] = "low"

    for town in towns:
        if town not in warning_levels:
            warning_levels[town] = None

    return warning_levels
