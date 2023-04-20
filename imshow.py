from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FixedLocator
import matplotlib.pyplot as plt
from matplotlib.colors import  ListedColormap  # LinearSegmentedColormap
import numpy as np


def __make_cc_colormap():
	color_list = [(1.0,1.0,1.0), (0.0,0.0,0.0), (1.0,0.0,0.0), (0.0,1.0,0.0), 
				  (0.0,0.0,1.0), (1.0,1.0,0.0), (0.0,1.0,1.0), (1.0,0.0,1.0), 
				  (0.8,0.8,0.8), (0.5,0.5,0.5), (0.5,0.0,0.0), (0.5,0.5,0.0), 
				  (0.0,0.5,0.0), (0.5,0.0,0.5), (0.0,0.5,0.5), (0.0,0.0,0.5)]

	return len(color_list), ListedColormap(color_list)

def cc_imshow(f, limit_npixel=400):
	height, width = f.shape
	vmax, cm = __make_cc_colormap()

	if height*width <= limit_npixel:
		__binary_imshow_with_grid(f, width, height, cmap=cm, vmin=0, vmax=vmax)
	else:
		plt.imshow(f, interpolation='none', cmap=cm, vmin=0, vmax=vmax)


def binary_imshow(f, limit_npixel=400):
	height, width = f.shape
	
	if height*width <= limit_npixel:
		__binary_imshow_with_grid(f, width, height, cmap='binary', vmin=0, vmax=f.max())
	else:
		plt.imshow(f, interpolation='none', cmap='binary', vmin=0, vmax=f.max())


def grayscale_imshow(f, limit_npixel=400):
	height, width = f.shape

	if height*width <= limit_npixel:
		__binary_imshow_with_grid(f, width, height, cmap='gray', vmin=0, vmax=f.max())
	else:
		plt.imshow(f, interpolation='none', cmap='gray', vmin=0, vmax=f.max())		

def __binary_imshow_with_grid(f, width, height, cmap='binary', vmin=0, vmax=255):
	ax = plt.gca()
	# ax.set_xticks(np.arange(width+1))
	# ax.set_yticks(np.arange(height))
	ax.set_xticklabels([], minor=False)
	ax.set_yticklabels([], minor=False)

	ax.set_xticklabels(np.arange(width+1), minor=True)
	ax.set_yticklabels(np.arange(height+1), minor=True)
		
	xminor_locator = AutoMinorLocator(2)
	yminor_locator = AutoMinorLocator(2)
	ax.xaxis.set_minor_locator(xminor_locator)
	ax.yaxis.set_minor_locator(yminor_locator)

	ax.grid(linestyle="dashed")
	extent = (0, width, height, 0)
	ax.imshow(f, interpolation='none', cmap=cmap, extent=extent, vmin=vmin, vmax=vmax)