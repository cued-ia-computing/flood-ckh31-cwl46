""" This module contains functions to computer least-square fit
of a polynomial to water level data.

"""

from matplotlib import dates as mpldates
import numpy as np
import datetime


def polyfit(dates, levels, p):
    """Take lists of dates and levels, and an integer p as the
    degree of polynomial. Compute least-square fit of a polynomial
    for the water level data supplied. Return a NumPy.poly1D object
    and shift in date axis.

    """

    d0 = dates[-1]
    mpl_dates = np.array(mpldates.date2num(dates)) - mpldates.date2num(d0)
    coeff = np.polyfit(mpl_dates, levels, p)
    poly = np.poly1d(coeff)
    return poly, d0


def prediction(poly, dates, d0):
    """Take a fitted Numpy.poly1D object, a list of dates and shift
    in date axis. Return a list of predicted water level data 15 minutes,
    1 hour, 2 hours, 6 hours, 12 hours and 24 hours ahead with values arranged
    in chronological order.

    """

    dates.sort()
    date = dates[-1]
    times = [15, 60, 120, 360, 720, 1440]

    prediction_time = [date + datetime.timedelta(minutes=time) for time in times]
    mpl_dates = np.array(mpldates.date2num(prediction_time)) - mpldates.date2num(d0)
    return poly(mpl_dates)
