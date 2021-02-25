
from .station import MonitoringStation
from datetime import date
from .utils import sorted_by_key
from .stationdata import build_station_list

def stations_level_over_threshold(stations, tol):

    stations = build_station_list()
    F = []
    r = [station.relative_water_level() for station in stations]
    i = 0
    
    for station in stations:
        q = (station.name, r[i])
        if r[i] > tol:
            F.append(q)
            i += 1
        else:
            i += 1
    
    F = sorted_by_key(F, 1)
    return F


def stations_highest_rel_level(stations, N):

    stations = build_station_list()
    r = [station.relative_water_level() for station in stations]
    i = 0
    S = []
    L = []

    for station in stations:
        q = (station.name, r[i])
        S.append(q)

    S = sorted_by_key(S,1)

    for i in range(N):
        L.append(S[i])
        i +=1
    return L
