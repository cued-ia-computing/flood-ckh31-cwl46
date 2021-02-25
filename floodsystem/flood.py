
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

    return [s[0] for s in S[:N]]
