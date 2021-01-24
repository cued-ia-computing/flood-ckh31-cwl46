# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["some station", "another station"]
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label[0]
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town
    assert repr(s) is not None


def test_decorators():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = ["some station", "another station"]
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

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
        s.latest_level = 0

    except AttributeError:
        raise AssertionError("latest_level cannot be changed.")
