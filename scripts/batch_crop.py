# Crops the given deck.gl HeatmapLayer JSON file to the given
# geographic zone as specified by latitude & longitude bounds

import json
import os
import sys

from crop_HeatmapLayer_JSON import crop

# ------------------------------------------------------------------------------

# name = "Asia1"
# bounds = 78.354492, 112.192382, 7.23169871, 31.61596594
# name = "US_SW"
# bounds = -123.7256004, -108.486937, 30.880233, 38.332099
# name = "Korea"
# bounds = 124.347356, 130.001543, 33.025503, 39.191307
# name = "SAfrica"
# bounds = 13.647156, 34.087810, -33.989610, -21.790521
# name = "Mexico"
# bounds = -117.650302, -86.411081, 13.696082, 32.687662
name = "SAMerica"
bounds = -73.807854, 29.585134, -35.160549, 2.699517

min_year = 1992
max_year = 2018

for year in range(min_year, max_year+1):

  in_path = "Harmonized_NTL/NTL_{}_1.json".format(year)
  min_lon, max_lon, min_lat, max_lat = bounds
  out_path = "Harmonized_NTL/{}_{}_1km.json".format(name, year)

  print()
  crop(in_path, min_lon, max_lon, min_lat, max_lat, out_path=out_path)
