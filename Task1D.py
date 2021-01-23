from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1D"""

    stations = build_station_list()

    rivers = rivers_with_station(stations)

    print(len(rivers))
    print(rivers[:10])

    print(sorted([station.name for station in stations_by_river(stations)['River Aire']]))
    print(sorted([station.name for station in stations_by_river(stations)['River Cam']]))
    print(sorted([station.name for station in stations_by_river(stations)['River Thames']]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
