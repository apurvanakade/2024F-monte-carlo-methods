import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate random data
x = np.random.normal(size=1000)
y = np.random.normal(size=1000)
z = np.random.normal(size=1000)

# Create 2D histogram
hist, xedges, yedges = np.histogram2d(x, y, bins=30)

# Compute the positions of the bars
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the bars
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

# Create the figure and the 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the 3D bar plot
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

# Label axes
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Histogram')

# Show the plot
plt.show()
