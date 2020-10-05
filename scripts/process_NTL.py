import os
import sys

import matplotlib.pyplot as plt
import rasterio

# ==============================================================================

def convert_NTL_to_JSON(in_path, stride=1, out_path=None):

  stride = int(stride)

  with rasterio.open(in_path) as dataset:

    if out_path is None:
      basedir, fname = os.path.split(in_path)
      year = fname.split("_")[3]
      fname = "NTL_{}_{}.json".format(year, stride)
      out_path = os.path.join(basedir, fname)
      assert out_path != in_path

    fout = open(out_path, "w")
    fout.write("[")

    data = dataset.read(1)
    NX, NY = data.shape

    next_i = NX // 10
    first = True
    for i in range(0, NX, stride):
      for j in range(0, NY, stride):
        if data[i,j] == 0:
          continue
        x, y = dataset.xy(i, j)
        s = '{{"COORDINATES": [{:.3f}, {:.3f}], "WEIGHT": {}}}'.format(x, y, data[i,j])
        if first:
          first = False
        else:
          fout.write(",")
        fout.write("\n" + s)
      if (i+1 >= next_i):
        print("{}/{}".format(i+1, NX))
        next_i += NX//10

    fout.write("\n]")
    fout.close()
    print("Wrote", out_path)

# ==============================================================================

if __name__ == "__main__":

  in_path = sys.argv[1]
  stride = int(sys.argv[2])

  convert_NTL_to_JSON(in_path, stride)
