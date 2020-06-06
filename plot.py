#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt

# <0.05 = red
# >=0.05 = light to dark grey

bucket = [
	{'min':2,'color':'#555555','xs':[],'ys':[]},
	{'min':1,'color':'#666666','xs':[],'ys':[]},
	{'min':0.5,'color':'#777777','xs':[],'ys':[]},
	{'min':0.25,'color':'#888888','xs':[],'ys':[]},
	{'min':0.05,'color':'#999999','xs':[],'ys':[]},
	{'min':0.0,'color':'#ff0000','xs':[],'ys':[]},
]

if len(sys.argv) < 2:
	print('Usage: %s MAplot.tsv' % sys.argv[0])
	sys.exit(1)
filename = sys.argv[1]

fig, ax = plt.subplots()
with open(filename) as f:
	lines = f.readlines()
	for line in lines:
		data = line.rstrip().split("\t")
		if data[0] == 'Chr': continue # Ignore the header
		y = float(data[4]) # Fold
		c = float(data[5]) # FDR
		x = float(data[6]) # log10_Mean_normalized_countd
		for data in bucket:
			if c > data['min']:
				data['xs'].append(x)
				data['ys'].append(y)
				break

	for data in bucket:
		ax.scatter(data['xs'], data['ys'], s=25, c=data['color'], alpha=0.3)

plt.xticks(np.arange(1.0,4.5,0.5))
plt.show()
