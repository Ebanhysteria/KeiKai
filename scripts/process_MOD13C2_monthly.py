import glob
import os
import sys

import numpy as np
from pyhdf.SD import SD, SDC

import matplotlib.pyplot as plt

# ----------------------------------------------------

def process_year(year, threshold, resolution):

  if resolution == 5:
    stride = 1
  elif resolution == 10:
    stride = 2
  elif resolution == 100:
    stride = 20
  else:
    print("resolution must be 5, 10, or 100")
    sys.exit()

  year_avg = np.zeros((3600, 7200))

  pattern = os.path.join(data_dir, "MOD13C2.A{}*.*.*.hdf".format(year))
  fpaths = sorted(glob.glob(pattern))
  N = len(fpaths)
  for fpath in fpaths:

    print(fpath)

    f = SD(fpath, SDC.READ)

    #for idx, sds in enumerate(f.datasets().keys()):
    #    print(idx, sds)

    data = f.select(ds_name).get()
    fill_value = f.select(ds_name).attributes()['_FillValue']
    scale = f.select(ds_name).attributes()['scale_factor']
    data = data.astype("float")
    data = data / scale
    #data[data <= fill_value/scale] = np.nan

    #print(data.shape)
    #print(data)
    #print(np.nanmin(data), np.nanmax(data))

    year_avg += data/N

  if threshold:
    year_avg[year_avg < threshold] = 0

  year_avg = np.transpose(year_avg)

  # Save full numpy array to disk
  out_path = os.path.join(data_dir, "EVI_{}_{}km.npy".format(year, resolution))
  np.save(out_path, year_avg)
  print("Wrote", out_path)

  # Open JSON file
  out_path = os.path.join(data_dir, "EVI_{}_{}km.json".format(year, resolution))
  fout = open(out_path, "w")
  fout.write("[")

  NX, NY = 7200, 3600
  next_i = NX // 10
  first = True
  for i in range(0, NX, stride):
    for j in range(0, NY, stride):
      if year_avg[i,j] == 0:
        continue
      lon, lat = CMG_lons[i], CMG_lats[j]
      s = '{{"COORDINATES": [{:.3f}, {:.3f}], "WEIGHT": {:.5f}}}'.format(lon, lat, year_avg[i,j])
      if first:
        first = False
      else:
        fout.write(",")
      fout.write("\n" + s)
    if (i+1 >= next_i):
      print("{}/{}".format(i+1, NX))
      next_i += NX//10

  # plt.imshow(year_avg, cmap="magma")
  # plt.show()

  fout.write("\n]")
  fout.close()
  print("Wrote", out_path)


# ----------------------------------------------------

if __name__ == "__main__":

  # MODIS CMG coords (GCTP_GEO)
  CMG_lats = -1*np.linspace(-90+0.05/2, 90-0.05/2, 3600)
  CMG_lons = np.linspace(-180+0.05/2, 180-0.05/2, 7200)

  data_dir = "MOD13C2"
  ds_name = "CMG 0.05 Deg Monthly EVI"
  year = sys.argv[1]
  threshold = 0.1
  resolution = 10   # Either 5, 10 or 100

  process_year(year, threshold, resolution)
