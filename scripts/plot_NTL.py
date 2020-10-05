import glob
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import rasterio

# ----------------------------------------------------

in_path = sys.argv[1]
basename, fname = os.path.splitext(in_path)
year = in_path.split("_")[1]

with rasterio.open(in_path) as dataset:

  data = dataset.read(1)
  NX, NY = data.shape

plt.figure(figsize=(14,7))
plt.imshow(data, cmap="inferno")
plt.title(fname)
plt.tight_layout()

if "--save" in sys.argv:
  out_fname = fname.replace(".npy", ".png")
  plt.savefig(out_fname)
  print("Wrote", out_fname)
else:
  plt.show()
