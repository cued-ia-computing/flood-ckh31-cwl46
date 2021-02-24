
from .station import MonitoringStation, relative_water_level, typical_range_consistent
from datetime import date
from .utils import sorted_by_key
from .stationdata import build_station_list

def stations_level_over_threshold(stations, tol):

    stations = build_station_list()
    F = []
    r = relative_water_level(stations)
    
    for station in stations:
        if typical_range_consistent(stations) is True:
            if r > tol:
                t = (station.name, r)
                F.append(t)
            else:
                ""
            F = sorted_by_key(F, 1)
        else:
            ""
    return F


def stations_highest_rel_level(stations, N):

    stations = build_station_list()
    r = relative_water_level(stations)
    i = 0
    S = []
    L = []

    for station in stations:
        q = (station.name, r)
        S.append(q)

    S = sorted_by_key(S,1)

    for i in range(N):
        L.append(S[i])
    return L
