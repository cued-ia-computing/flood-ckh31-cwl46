
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
            return F
        else:
            ""