import sys
import warnings
import re


peak_f = sys.stdin


distance =0

for line in peak_f:
	line = line.replace('\n', '')
	line_l = re.split('\t', line)
	distance = distance +int(line_l[2])-int(line_l[1])

print (distance)

