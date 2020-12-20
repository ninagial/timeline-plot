import argparse
from itertools import combinations
import datetime
from classes import *
from entries import entries
from funcs import *

# allow passing arguments in the command line
parser = argparse.ArgumentParser()
parser.add_argument("--start", "-s", help="timeline start date")
parser.add_argument("--end", "-e", help="timeline end date")
args = parser.parse_args()

# sort entries chronologically
entries_t = sorted(entries, key=lambda entry: entry.date)

# limit entries to a specific date range (otherwise use defaults)
if args.start:
    date_range_start = args.start
else:
    date_range_start= "2017-07-01"

if args.end:
    date_range_end = args.end
else:
    date_range_end = "2020-12-31"

entries_f = list(filter(lambda e: logical_date_range(e, start=date_range_start, end=date_range_end), entries_t))

for i in entries_t:
    print(str(i))

names = ["{0}-({2} {1})".format(x.label, x.date.month , x.date.day) for x in entries_f]
dates = [x.date for x in entries_f]

draw_plot(names=names, dates=dates, dr_start=date_range_start, dr_end=date_range_end)
