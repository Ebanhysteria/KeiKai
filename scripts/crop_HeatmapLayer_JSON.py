# Crops the given deck.gl HeatmapLayer JSON file to the given
# geographic zone as specified by latitude & longitude bounds

import json
import os
import sys

# ------------------------------------------------------------------------------

def crop(in_path, min_lon, max_lon, min_lat, max_lat, out_path=None):

  if out_path is None:
    base, ext = os.path.splitext(in_path)
    out_path = base + "_crop.json"

  print("Cropping {} ...".format(in_path))
  fin = open(in_path)
  fout = open(out_path, "w")
  fout.write("[")
  lines_count = 0
  out_count = 0
  for line in fin:
    line = line.strip()
    lines_count += 1
    if "COORDINATES" in line:
      line = line.strip(',')
      data = json.loads(line)
      lon = float(data["COORDINATES"][0])
      lat = float(data["COORDINATES"][1])
      if min_lon <= lon <= max_lon and min_lat <= lat <= max_lat:
        if out_count > 0:
          fout.write(",")
        fout.write("\n" + line)
        out_count += 1
  fout.write("\n]")

  fin.close()
  fout.close()

  print("Wrote {:,} points to {}".format(out_count, out_path))

# ------------------------------------------------------------------------------

# Some bounding boxes:
# United States: 119.531111 73.300833 25.403611 49.818055
# Mexico: -117.12776 -86.811982388 14.5388286402 32.72083
# Australia: 113.338953078 153.569469029 -43.6345972634 -10.6681857235

if __name__ == "__main__":

  if len(sys.argv) != 6:
    print("Usage:")
    print("  python3 crop_HeatmapLayer_JSON.py <JSON file> <min longitude> <max longitude> <min latitude> <max latitude>")
    print("\nLatitude and longitude in decimal degrees, negative for west longitudes and south latitudes.")
    sys.exit()

  in_path = sys.argv[1]
  min_lon = float(sys.argv[2])
  max_lon = float(sys.argv[3])
  min_lat = float(sys.argv[4])
  max_lat = float(sys.argv[5])

  crop(in_path, min_lon, max_lon, min_lat, max_lat, out_path=None)
