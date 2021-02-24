# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from datetime import date


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["some station", "another station"]
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    evalues = (-10, 10)
    catchment = "some catchment"
    date_open = date(1970, 1, 1)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, evalues, river, town, catchment, date_open)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label[0]
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.extreme_values == evalues
    assert s.river == river
    assert s.town == town
    assert s.catchment == catchment
    assert s.date_open == date_open
    assert repr(s) is not None


def test_decorators():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["some station", "another station"]
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    evalues = (-10, 10)
    catchment = "some catchment"
    date_open = date(1970, 1, 1)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, evalues, river, town, catchment, date_open)

    try:
        s.station_id = "changed"
        raise AssertionError("station_id can be changed.")

    except AttributeError:
        pass

    try:
        s.measure_id = "changed"
        raise AssertionError("measure_id can be changed.")

    except AttributeError:
        pass

    try:
        s.name = "changed"
        raise AssertionError("name can be changed.")

    except AttributeError:
        pass

    try:
        s.coord = "changed"
        raise AssertionError("coord can be changed.")

    except AttributeError:
        pass

    try:
        s.typical_range = "changed"
        raise AssertionError("typical_range can be changed.")

    except AttributeError:
        pass

    try:
        s.extreme_values = "changed"
        raise AssertionError("extreme_values can be changed.")

    except AttributeError:
        pass

    try:
        s.river = "changed"
        raise AssertionError("river can be changed.")

    except AttributeError:
        pass

    try:
        s.town = "changed"
        raise AssertionError("town can be changed.")

    except AttributeError:
        pass

    try:
        s.catchment = "changed"
        raise AssertionError("catchment can be changed.")

    except AttributeError:
        pass

    try:
        s.date_open = "changed"
        raise AssertionError("date_open date can be changed.")

    except AttributeError:
        pass

    assert s.latest_level is None

    try:
        s.latest_level = 0

    except AttributeError:
        raise AssertionError("latest_level cannot be changed.")


def test_typical_range_consistent():

    # Create stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["some station", "another station"]
    coord = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    trange2 = (3.4445, 3.4445)
    trange3 = (-2.3, -3.4445)
    trange4 = None
    evalues = (-10, 10)
    catchment = "some catchment"
    date_open = date(1970, 1, 1)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, evalues, river, town, catchment, date_open)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, evalues, river, town, catchment, date_open)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, evalues, river, town, catchment, date_open)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange4, evalues, river, town, catchment, date_open)

    assert s1.typical_range_consistent() is True
    assert s2.typical_range_consistent() is True
    assert s3.typical_range_consistent() is False
    assert s4.typical_range_consistent() is False


def test_inconsistent_typical_range_stations():

    # Create stations
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["some station", "another station"]
    coord = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    trange2 = (3.4445, 3.4445)
    trange3 = (-2.3, -3.4445)
    trange4 = None
    evalues = (-10, 10)
    catchment = "some catchment"
    date_open = date(1970, 1, 1)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, evalues, river, town, catchment, date_open)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, evalues, river, town, catchment, date_open)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, evalues, river, town, catchment, date_open)
    s4 = MonitoringStation(s_id, m_id, label, coord, trange4, evalues, river, town, catchment, date_open)

    stations = [s1, s2, s3, s4]

    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert type(inconsistent_stations) == list
    assert len(inconsistent_stations) == 2
    assert (type(station) == MonitoringStation for station in inconsistent_stations)
    assert inconsistent_stations == [s3, s4]
