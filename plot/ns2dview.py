import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import argparse as arg


parser = arg.ArgumentParser(description='Visualize a radial profile of a star')
parser.add_argument(
    '-p', '--pdf', help='Path for resulting figure', default="temp.pdf")
parser.add_argument('-c', '--csv', help='Path to radial profile csv')
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

FullFunction = f(rmesh, thetamesh)

fig, ax = plt.subplots(dpi=120, subplot_kw=dict(projection='polar'))
ax.contourf(thetamesh, rmesh, FullFunction, 100, cmap='plasma')

plt.savefig(args.pdf)
plt.show()
