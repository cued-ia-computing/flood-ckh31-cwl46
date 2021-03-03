"""This module provides a visualisation of
MonitoringStations data through plots on maps.

"""

import plotly.graph_objects as go


def location_map(stations):
    """Take the list of monitoring station as MonitoringStation objects
    and plot their positions in a Plotly map.

    """

    mapbox_access_token = "pk.eyJ1IjoiY3dsNDYiLCJhIjoiY2traDVqMzk5MTl1eDJ4cXQ3eG52ODZ5cCJ9.vvdhnwVwPVAZF0OWryqWVg"

    fig = go.Figure(go.Scattermapbox(
        lat=[station.coord[0] for station in stations],
        lon=[station.coord[1] for station in stations],
        mode='markers',
        marker=go.scattermapbox.Marker(size=5, color='rgb(200,100,0)'),
        text=[station.name for station in stations]
    ))

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            style='outdoors',
            center=dict(lat=52.89, lon=-1.56),
            pitch=0,
            zoom=5)
    )

    fig.show()
    return None


def location_rel_level_map(stations):
    """Take the list of monitoring station as MonitoringStation objects
    and plot their positions in a Plotly map with colours identifying
    their relative level.

    """

    mapbox_access_token = "pk.eyJ1IjoiY3dsNDYiLCJhIjoiY2traDVqMzk5MTl1eDJ4cXQ3eG52ODZ5cCJ9.vvdhnwVwPVAZF0OWryqWVg"

    stationsA = [station for station in stations if station.relative_water_level() is None]
    stationsB = [station for station in stations if station.relative_water_level() is not None]
    stations1 = [station for station in stationsB if station.relative_water_level() < 0.0]
    stations2 = [station for station in stationsB if station.relative_water_level() > 0.0
                 and station.relative_water_level() < 1.0]
    stations3 = [station for station in stationsB if station.relative_water_level() > 1.0]

    fig = go.Figure(go.Scattermapbox(
        lat=[station.coord[0] for station in stationsA],
        lon=[station.coord[1] for station in stationsA],
        mode='markers',
        marker=go.scattermapbox.Marker(size=5, color='rgb(0,0,0)'),
        text=[station.name for station in stationsA],
        name="DataError"
    ))

    fig.add_trace(go.Scattermapbox(
        lat=[station.coord[0] for station in stations1],
        lon=[station.coord[1] for station in stations1],
        mode='markers',
        marker=go.scattermapbox.Marker(size=5, color='rgb(200,100,0)'),
        text=[station.name + " " + str(round(station.relative_water_level(), 3)) for station in stations1],
        name="Below Typical"
    ))

    fig.add_trace(go.Scattermapbox(
        lat=[station.coord[0] for station in stations2],
        lon=[station.coord[1] for station in stations2],
        mode='markers',
        marker=go.scattermapbox.Marker(size=5, color='rgb(50,220,50)'),
        text=[station.name + " " + str(round(station.relative_water_level(), 3)) for station in stations2],
        name="Within Typical"
    ))

    fig.add_trace(go.Scattermapbox(
        lat=[station.coord[0] for station in stations3],
        lon=[station.coord[1] for station in stations3],
        mode='markers',
        marker=go.scattermapbox.Marker(size=5, color='rgb(220,50,50)'),
        text=[station.name + " " + str(round(station.relative_water_level(), 3)) for station in stations3],
        name="Above Typical"
    ))

    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            style='outdoors',
            center=dict(lat=52.89, lon=-1.56),
            pitch=0,
            zoom=5)
    )

    fig.show()
    return None
