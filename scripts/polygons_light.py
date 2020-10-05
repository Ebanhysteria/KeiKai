import glob
import sys

import numpy as np
import rasterio
from rasterstats import zonal_stats

polygons_path = sys.argv[1]

start_year = 1992
end_year = 2018

categories = [(0, 63), (0, 9), (10, 29), (30, 63)]

years = range(start_year, end_year+1)
data = []
for year in years:

  light_fpath = glob.glob("Harmonized_NTL/Harmonized_DN_NTL_{}_*.tif".format(year))[0]

  img = rasterio.open(light_fpath)
  light = img.read(1)
  light_copy = np.copy(light)

  # Total light
  stats = zonal_stats(polygons_path, light, affine=img.transform, stats="sum", nodata=0)
  sum_total = sum([x['sum'] for x in stats if x['sum'] is not None])

  # By categories
  totals = [sum_total]
  for x1, x2 in categories:
    mask = (light >= x1) & (light <= x2)
    light_copy[mask] = 1
    light_copy[~mask] = 0
    stats = zonal_stats(polygons_path, light_copy, affine=img.transform, stats="sum", nodata=0)
    total = sum([x['sum'] for x in stats if x['sum'] is not None])
    totals.append(total)

  print("{},{}".format(year, ",".join(["{:.0f}".format(x) for x in totals])))
