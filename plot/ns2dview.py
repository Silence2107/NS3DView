import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import ticker
import pandas as pd
from scipy import interpolate
import argparse as arg


parser = arg.ArgumentParser(description='Visualize a radial profile of a star')
# IO opts
parser.add_argument(
    '-p', '--pdf', help='Path for resulting figure', default="temp.pdf")
parser.add_argument('-c', '--csv', help='Path to radial profile csv')
parser.add_argument(
    '--header', help='use if the csv has a header', action='store_true')
parser.add_argument('--sep', help='separator for csv', default=',', type=str)
parser.add_argument('--cols', help='columns to use',
                    default=[0, 1], type=int, nargs=2)
# draw opts
parser.add_argument('--log', help='Use log scale', action='store_true')
parser.add_argument(
    '--legend', help='Provide header for legend', default=None, type=str)
parser.add_argument('--labels', help='Provide labels for the axes',
                    default=None, type=str, nargs=2)
parser.add_argument('--limits', help='Provide limits for the z-axis',
                    default=None, type=float, nargs=2)

args = parser.parse_args()

dataset = pd.read_csv(args.csv, sep=args.sep,
                      usecols=args.cols, header=0 if args.header else None)

labels = args.labels if args.labels is not None else dataset.columns

# get the radial values
rlist = dataset.iloc[:, 0]
vallist = dataset.iloc[:, 1]

interp = interpolate.interp1d(
    x=rlist,
    y=vallist,
    kind='linear')

thetalist = np.radians(np.arange(0, 361, 5))

def f(r, theta):
    return interp(r)

rmesh, thetamesh = np.meshgrid(rlist, thetalist)

z = f(rmesh, thetamesh)

limits = args.limits if args.limits is not None else [z.min(), z.max()]

fig, ax = plt.subplots(dpi=120, subplot_kw=dict(projection='polar'))
if args.log:
    z = np.ma.masked_where(z <= 0, z)
    profile = ax.pcolor(thetamesh, rmesh, z, cmap='plasma', norm=matplotlib.colors.LogNorm(
        vmin=limits[0], vmax=limits[1]), shading='auto', rasterized=True)
else:
    profile = ax.pcolor(thetamesh, rmesh, z, cmap='plasma', norm=matplotlib.colors.Normalize(
        vmin=limits[0], vmax=limits[1]), shading='auto', rasterized=True)
# ax.set_yticklabels([])
ax.set_xticklabels([])
# colorbar
cbar = plt.colorbar(profile, ax=ax)
if args.legend:
    cbar.set_label(labels[1] + ',' + args.legend)

# axis labels from dataset
ax.set_xlabel(labels[0])

plt.savefig(args.pdf)
plt.show()
