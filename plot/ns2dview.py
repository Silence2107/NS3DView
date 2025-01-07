import numpy as np

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import ticker
import pandas as pd
from scipy import interpolate
import argparse as arg


parser = arg.ArgumentParser(description='Visualize a radial profile of a star')
parser.add_argument(
    '-p', '--pdf', help='Path for resulting figure', default="temp.pdf")
parser.add_argument('-c', '--csv', help='Path to radial profile csv')
# draw opts
parser.add_argument('--levels', help='Number of color levels', default=20, type=int)
parser.add_argument('--log', help='Use log scale', action='store_true')
parser.add_argument('--legend', help='Provide header for legend', default=None, type=str)

args = parser.parse_args()


dataset=pd.read_csv(args.csv,index_col=0)

# Lest imagine fro a minute that what we are seing is : we are fixing a maximum mass of M=1.4 and a massimum radius of R=12 and
# we are seing the pressure changing with the radius of the star

# get the radial values
rlist = dataset.iloc[:, 0]
vallist = dataset.iloc[:, 1]

interp = interpolate.interp1d(
    x=rlist,
    y=vallist,
    kind='linear')

thetalist = np.radians(np.arange(0, 361, 1))

def f(r, theta):
    return interp(r)

rmesh, thetamesh = np.meshgrid(rlist, thetalist)

z = f(rmesh, thetamesh)

fig, ax = plt.subplots(dpi=120, subplot_kw=dict(projection='polar'))
if args.log:
    z = np.ma.masked_where(z <= 0, z)
    profile = ax.contourf(thetamesh, rmesh, z, args.levels, cmap='plasma', locator=ticker.LogLocator())
else:
    profile = ax.contourf(thetamesh, rmesh, z, args.levels, cmap='plasma')
ax.set_yticklabels([])
ax.set_xticklabels([])
#colorbar
cbar = plt.colorbar(profile, ax=ax)
if args.legend:
    cbar.set_label(args.legend)

plt.savefig(args.pdf)
plt.show()
