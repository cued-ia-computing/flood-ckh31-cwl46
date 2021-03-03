from floodsystem.flood import station_risk
from floodsystem.stationdata import build_station_list, update_water_levels


def run():

    stations = build_station_list()
    update_water_levels(stations)

    v = station_risk(stations)

    print(v)


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
