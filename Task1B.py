from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():

    stations = build_station_list()
    p = (52.2053, 0.1218)

    List = stations_by_distance(stations, p)

    print(List[:10])
    print(List[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
