import numpy as np
import matplotlib.pyplot as plt

def f(r, theta):
    return r * np.cos(theta)

rlist=np.arange(0,1.01,0.01)
thetalist=np.radians(np.arange(0,361,1))
rmesh, thetamesh = np.meshgrid(rlist, thetalist)

FullFunction = f(rmesh, thetamesh)

fig, ax = plt.subplots(dpi=120,subplot_kw=dict(projection='polar'))
ax.contourf(thetamesh, rmesh, FullFunction, 100, cmap='plasma')

plt.savefig('temp.pdf')
plt.show()