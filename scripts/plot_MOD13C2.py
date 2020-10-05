import glob
import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------

fname = sys.argv[1]
data = np.load(fname).T

year = fname.split("_")[1]

plt.figure(figsize=(14,7))
plt.imshow(data, cmap="cubehelix", extent=[-180, 180, -90, 90])
plt.title(fname)
plt.tight_layout()

if "--save" in sys.argv:
  out_fname = fname.replace(".npy", ".png")
  plt.savefig(out_fname)
  print("Wrote", out_fname)
else:
  plt.show()
