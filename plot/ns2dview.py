import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from scipy import interpolate
import argparse as arg


parser = arg.ArgumentParser(description='Description of your program')
parser.add_argument('-p','--pdf', help='Description for foo argument', default="temp.pdf")
parser.add_argument('-c','--csv', help='Description for bar argument', default='./data/data.csv')
args = parser.parse_args()


dataset=pd.read_csv(args.csv,index_col=0)

# Lest imagine fro a minute that what we are seing is : we are fixing a maximum mass of M=1.4 and a massimum radius of R=12 and 
# we are seing the pressure changing with the radius of the star 

rlist=np.arange(0,1.01,0.01)

interp=interpolate.interp1d(
        x=dataset.iloc[:,0],
        y=dataset.iloc[:,1],
        kind=   'linear')

thetalist=np.radians(np.arange(0,361,1))

def f(r, theta):
    return interp(r)

rmesh, thetamesh = np.meshgrid(rlist, thetalist)

FullFunction = f(rmesh, thetamesh)

fig, ax = plt.subplots(dpi=120,subplot_kw=dict(projection='polar'))
ax.contourf(thetamesh, rmesh, FullFunction, 100, cmap='plasma')

plt.savefig(args.pdf)
plt.show()