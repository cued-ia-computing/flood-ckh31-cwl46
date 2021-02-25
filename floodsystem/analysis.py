""" This module contains functions to computer least-square fit
of a polynomial to water level data.

"""

from matplotlib import dates as mpldates
import numpy as np


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
