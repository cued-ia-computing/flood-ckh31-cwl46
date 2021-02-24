from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def run():

    stations = build_station_list()
    N = 10
    
    v = stations_highest_rel_level(stations, N)

    print(v)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
