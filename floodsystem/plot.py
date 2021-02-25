""" This module provides interface for visualising data collected
from the Internet.

"""

from matplotlib import pyplot as plt, dates as mpldates
import numpy as np
from .analysis import polyfit
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def plot_water_levels(station, dates, levels):
    """ Take a MonitoringStation object and lists of dates and water
    levels. Show plots of station readings, typical low and high values.
    Return None.

    """

    typical_low = np.ones(len(dates)) * station.typical_range[0]
    typical_high = np.ones(len(dates)) * station.typical_range[1]

    plt.plot(dates, levels, '-r', label='station readings')
    plt.plot(dates, typical_low, '--m', label='typical low')
    plt.plot(dates, typical_high, '--b', label='typical high')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

    return None


def plot_water_levels_ext(stations, datess, levelss, p):
    """ Take a list of at most 6 MonitoringStation objects, a list of respective
    lists of dates, a list of respective lists of water levels and an integer p
    as the degree of polynomial. Show at most 6 plots of station readings, typical
    low and high values, and the best-fit polynomial in the same window.
    Return None.

    """

    for i in range(len(stations)):
        s = plt.subplot(2, 3, i + 1)
        typical_low = np.ones(len(datess[i])) * stations[i].typical_range[0]
        typical_high = np.ones(len(datess[i])) * stations[i].typical_range[1]

        poly, d0 = polyfit(datess[i], levelss[i], p)
        t0 = np.ones(len(datess[i])) * mpldates.date2num(d0)
        mpl_dates = mpldates.date2num(datess[i]) - t0

        s.plot(datess[i], levelss[i], '-r', label='station readings')
        s.plot(datess[i], typical_low, '--k', label='typical low')
        s.plot(datess[i], typical_high, '--b', label='typical high')
        s.plot(datess[i], poly(np.array(mpl_dates)), '-g', label='best fit')
        s.set_xlabel('date')
        s.set_ylabel('water level (m)')
        # s.legend()
        s.tick_params(axis='x', labelrotation=45)
        s.set_title(stations[i].name)

    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.show()

    return None


def plot_water_levels_web(stations, datess, levelss, p):
    """ Take a list of at most 9 MonitoringStation objects, a list of respective
    lists of dates, a list of respective lists of water levels and an integer p
    as the degree of polynomial. Show at most 9 plots of station readings, typical
    low and high values, and the best-fit polynomial through Plotly.
    Return None.

    """
    fig = make_subplots(rows=3, cols=3, subplot_titles=[station.name for station in stations])

    for i in range(len(stations)):
        row = i // 3 + 1
        col = i % 3 + 1

        typical_low = np.ones(len(datess[i])) * stations[i].typical_range[0]
        typical_high = np.ones(len(datess[i])) * stations[i].typical_range[1]

        poly, d0 = polyfit(datess[i], levelss[i], p)
        t0 = np.ones(len(datess[i])) * mpldates.date2num(d0)
        mpl_dates = mpldates.date2num(datess[i]) - t0

        fig.add_trace(go.Scatter(x=datess[i], y=levelss[i], line=dict(color='orange', width=3)), row, col)
        fig.add_trace(go.Scatter(x=datess[i], y=typical_low, line=dict(color='navy', width=1.5, dash='dash')), row, col)
        fig.add_trace(go.Scatter(x=datess[i], y=typical_high, line=dict(color='navy',
                                 width=1.5, dash='dash')), row, col)
        fig.add_trace(go.Scatter(x=datess[i], y=poly(np.array(mpl_dates)), line=dict(color='green',
                                 width=3, dash='dot')), row, col)

        fig.update_yaxes(title_text="water level (m)", row=row, col=col)
        fig.update_layout(xaxis_range=[datess[i][0], datess[i][-1]])

    fig.update_layout(showlegend=False)
    fig.show()

    return None


def plot_water_level_with_fit(station, dates, levels, p):
    """ Take a MonitoringStation object, lists of dates and water levels
    and an integer p as the degree of polynomial. Show plots of station
    readings, typical low and high values and the best-fit polynomial.
    Return None.

    """

    poly, d0 = polyfit(dates, levels, p)
    t0 = np.ones(len(dates)) * mpldates.date2num(d0)
    typical_low = np.ones(len(dates)) * station.typical_range[0]
    typical_high = np.ones(len(dates)) * station.typical_range[1]

    mpl_dates = mpldates.date2num(dates) - t0

    plt.plot(dates, levels, '-r', label='station readings')
    plt.plot(dates, typical_low, '--m', label='typical low')
    plt.plot(dates, typical_high, '--b', label='typical high')
    plt.plot(dates, poly(np.array(mpl_dates)), '-g', label='best fit')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

    return None
