from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():

    stations = build_station_list()
    update_water_levels(stations)
    N = 10

    b = stations_highest_rel_level(stations, N)

    print(b)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
