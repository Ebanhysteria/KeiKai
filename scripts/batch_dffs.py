import glob
import sys

from NTL_diffs import compute_NTL_diffs


# ==============================================================================

#start_year = 1992
#end_year = 2018
start_year = 1992
end_year = 2007
stride = 10

# ---------------------------------------

fnames = []
for year in range(start_year, end_year+1):
  fn = glob.glob("Harmonized_NTL/Harmonized*_{}_*.tif".format(year))
  fnames.append(fn[0])

for i in range(len(fnames)-1):

  in_path1 = fnames[i]
  in_path2 = fnames[i+1]

  compute_NTL_diffs(in_path1, in_path2, stride)
