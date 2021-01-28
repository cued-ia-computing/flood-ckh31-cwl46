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
    return 0
