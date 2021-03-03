
from .utils import sorted_by_key


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
    No = []
    i = 0

    for station in stations:
        if r[i] is not None:
            if r[i] > 0:
                q = (station.name, r[i])
                S.append(q)
            else:
                f = (station.name, None)
                No.append(f)                    
        else:
            f = (station.name, r[i])
            No.append(f)
        i += 1

    S = sorted_by_key(S, 1, True)
    S.append(No)

    return S[:N]


def station_risk(stations):
    
    risk = ""
    r = [station.relative_water_level() for station in stations]
    S = []
    i = 0

    for station in stations:
        if r[i] is not None:
            if r[i] >= 5:
                risk = "Severe"
                q = {"Name":station.name, "Risk":risk}
                S.append(q)
            elif r[i] >= 3 and r[i] < 5:
                risk = "High"
                q = {"Name":station.name, "Risk":risk}
                S.append(q)
            elif r[i] >= 2 and r[i] < 3:
                risk = "Moderate"
                q = {"Rame":station.name, "Risk":risk}
                S.append(q)
            else:
                risk = "Low"
                q = {"Name":station.name, "Risk":risk}
                S.append(q)
        else:
            risk = "N/A"
            q = {"Name":station.name, "Risk":risk}
            S.append(q)
        i += 1
    return S
