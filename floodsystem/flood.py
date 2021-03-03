
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
    i = 0

    for station in stations:
        if r[i] is not None:
            q = (station, r[i])
            S.append(q)
        i += 1

    S = sorted_by_key(S, 1, True)

<<<<<<< HEAD
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
=======
    return [s[0] for s in S[:N]]
>>>>>>> 216a1c5ae82a40954d98ea2683ff90960b262fa7
