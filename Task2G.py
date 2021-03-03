from floodsystem.flood import update_stations_risk, update_flood_warnings
from floodsystem.stationdata import build_station_list, update_water_levels


def run():

    # List truncated to shorten runtime for testing
    stations = build_station_list()[:50]
    update_water_levels(stations)
    update_stations_risk(stations)

    towns = update_flood_warnings(stations)

    severe_list = sorted([town for town in towns if towns[town] == "severe"])
    high_list = sorted([town for town in towns if towns[town] == "high"])
    moderate_list = sorted([town for town in towns if towns[town] == "moderate"])
    low_list = sorted([town for town in towns if towns[town] == "low"])

    print("{} Towns with Severe Warning".format(len(severe_list)))
    print("{} Towns with High Warning".format(len(high_list)))
    print("{} Towns with Moderate Warning".format(len(moderate_list)))
    print("{} Towns with Low Warning".format(len(low_list)))
    print("Severe Warnings:")
    for town in severe_list:
        print(town)
    print("High Warnings:")
    for town in high_list:
        print(town)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
