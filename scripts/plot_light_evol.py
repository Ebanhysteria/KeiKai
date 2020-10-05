import sys

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd

plt.style.use('dark_background')

fpath = sys.argv[1]
region_name = sys.argv[2]

df = pd.read_csv(fpath)

if region_name == "Cambodia":
  light_ref = 10e3
elif region_name == "Laos":
  light_ref = 1000
else:
  light_ref = df["total_light"][0]

light_relative = 100*df["total_light"]/light_ref
plt.plot(df["Year"], light_relative)

plt.xlabel("Year")
plt.ylabel("Amount of artificial light (relative)")
plt.title("Evolution of artificial light in PAs in {}".format(region_name))
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.tight_layout()
plt.grid(ls=":")

if "--save" in sys.argv:
  fname = "{}_light_evol.png".format(region_name.replace(" ", "_"))
  plt.savefig(fname)
  print("Wrote", fname)
else:
  plt.show()
