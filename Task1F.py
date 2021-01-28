from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():

    stations = build_station_list

    W = [inconsistent_typical_range_stations(stations)]

    i = 0

    print(W)

    while i < len(W):
        T = [W[i]]
        Y = [T[0]]
        U = sorted(Y)
        i += 1
    return U


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
