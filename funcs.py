import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
import re
from entries import *


def logical_date_range(en, start='2019-08-31', end='2020-08-15'):
    """ Boolean, en is in Date range """
    after = en.date >= datetime.datetime.strptime(start, "%Y-%m-%d").date()
    before = en.date <= datetime.datetime.strptime(end, "%Y-%m-%d").date()
    return before and after

def draw_plot(names, dates, dr_start='', dr_end=''):
    # Define start and end dates
    dr_start = datetime.datetime.strptime(dr_start, "%Y-%m-%d").date()
    ms = dr_start.month
    ys = dr_start.year
    dr_end = datetime.datetime.strptime(dr_end, "%Y-%m-%d").date()
    me = dr_end.month
    ye = dr_end.year
    # Choose some nice levels
    levels = np.tile([-7, 7, -5, 5, -4, 4, -2, 2, -0.5, 0.5],
                     int(np.ceil(len(dates)/10)))[:len(dates)]
    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize=(8.8, 4), constrained_layout=True)
    ax.set(title="Trans Related Events")
    markerline, stemline, baseline = ax.stem(dates, levels,
                                             linefmt="C3-", basefmt="k-",
                                             use_line_collection=True)
    plt.setp(markerline, mec="k", mfc="w", zorder=3)
    # Shift the markers to the baseline by replacing the y-data by zeros.
    markerline.set_ydata(np.zeros(len(dates)))
    # annotate lines
    vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
    for d, l, r, va in zip(dates, levels, names, vert):
        ax.annotate(r, xy=(d, l), xytext=(-3, np.sign(l)*3),
                    textcoords="offset points", va=va, ha="right")
    # format xaxis 
    ax.get_xaxis().set_major_locator(mdates.YearLocator())
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%Y"))
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    # remove y axis and spines
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)
    ax.margins(y=0.1)
    plt.show()

