import os
import sys

import matplotlib.pyplot as plt
import rasterio

# ==============================================================================

def compute_NTL_diffs(in_path1, in_path2, stride=1, out_path=None):

  stride = int(stride)

  ds1 = rasterio.open(in_path1)
  ds2 = rasterio.open(in_path2)

  if out_path is None:
    basedir, fname1 = os.path.split(in_path1)
    year1 = fname1.split("_")[3]
    basedir, fname2 = os.path.split(in_path2)
    year2 = fname2.split("_")[3]
    fname = "NTL_{}_{}_{}.json".format(year1, year2, stride)
    out_path = os.path.join(basedir, fname)      
    assert out_path != in_path1
    assert out_path != in_path2

  fout = open(out_path, "w")
  fout.write("[")
     
  data1 = ds1.read(1).astype("int")
  data2 = ds2.read(1).astype("int")
  assert data1.shape == data2.shape
  if ds1.bounds != ds2.bounds:
    print("Geo bounds are different")
    deltas = [getattr(ds1.bounds, x)-getattr(ds2.bounds, x) for x in ["left", "bottom", "right", "top"]]
    if max(deltas) > 0.01:
      print(ds1.bounds)
      print(ds2.bounds)
      sys.exit()
    else:
      print("Acceptable difference")
    
  NX, NY = data1.shape

  diff = data2 - data1
  print(diff.max())

  next_i = NX // 10
  first = True
  for i in range(0, NX, stride):
    for j in range(0, NY, stride):
      if diff[i,j] == 0:
        continue
      x, y = ds1.xy(i, j)
      s = '{{"COORDINATES": [{:.3f}, {:.3f}], "WEIGHT": {}}}'.format(x, y, diff[i,j])
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

  in_path1 = sys.argv[1]
  in_path2 = sys.argv[2]
  stride = int(sys.argv[3])

  print(in_path1, in_path2)
  compute_NTL_diffs(in_path1, in_path2, stride)
