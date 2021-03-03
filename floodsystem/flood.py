
from .station import MonitoringStation
from datetime import date
from .utils import sorted_by_key
from .stationdata import build_station_list

def stations_level_over_threshold(stations, tol):

    F = []
    r = [station.relative_water_level() for station in stations]
    i = 0
    
    for station in stations:
        if r[i] != None:
            q = (station.name, r[i])
            if r[i] > tol:
                F.append(q)
                i += 1
            else:
                i += 1
        else:
            ""
    
    F = sorted_by_key(F, 1, True)
    return F


def stations_highest_rel_level(stations, N):

    r = [station.relative_water_level() for station in stations]
    S = []
    i = 0

    for station in stations:
        if r[i] != None:
            q = (station.name, r[i])
            S.append(q)
            i += 1
        else:
            ""

    S = sorted_by_key(S, 1, True)

    return S[:N]

def station_risk(stations):
    
    risk = ""
    r = [station.relative_water_level() for station in stations]
    S = []
    i = 0

    for station in stations:
        if r[i] > 5:
            risk = "Severe"
            q = {"Name":station.name, "Risk":risk}
            S.append(q)
        elif r[i] > 3:
            risk = "High"
            q = {"Name":station.name, "Risk":risk}
            S.append(q)
        elif r[i] > 2:
            risk = "Moderate"
            q = {"Rame":station.name, "Risk":risk}
            S.append(q)
        else:
            risk = "Low"
            q = {"Name":station.name, "Risk":risk}
            S.append(q)
    return S
