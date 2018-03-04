import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

x=np.array([0,1,1,0])
y=np.array([0,0,1,1])
plt.axis((-2,3,-2,3))
plt.grid(True)
plt.axes().set_aspect('equal','datalim')
plt.fill_between(x,y)
plt.show()

scale_trns = np.array([[1.5, 0], [0, 1.5]])
scaled_data = np.dot(scale_trns, np.vstack((x, y)))
scaled_data_x, scaled_data_y = scaled_data[0,:], scaled_data[1,:]
plt.axis((-2,3,-2,3))
plt.grid(True)
plt.axes().set_aspect('equal', 'datalim')
plt.fill_betweenx(scaled_data_x, scaled_data_y)
plt.show()

#Create a rectangle for this example:
verts = [
    (0., 0.), # left, bottom
    (0., 1.), # left, top
    (1., 1.), # right, top
    (1., 0.), # right, bottom
    ]
# Plotting Utility
codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         ]
path = Path(verts, codes)
def plot_poly(path):
    """
    Utility to plot the polygon
    """
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111,aspect='equal')
    patch = patches.PathPatch(path, facecolor='blue')
    ax.add_patch(patch)
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()
    return
