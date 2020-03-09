import csv
import sys
fl = sys.argv[1]
with open(fl,'r') as csvfile:
  data = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in data:
    print ', '.join(row)
