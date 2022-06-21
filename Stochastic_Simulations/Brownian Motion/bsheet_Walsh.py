# A simulation of a Brownian sheet though theory of Walsh

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Set the time and space intervals. Choose number of partitions of each.

# Time
t = 2
nt = 400
delta_t = t / nt

# Space
x = 2
nx = 400
delta_x = x / nx

# create the time and spatial axis
t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# Create the Brownian sheet noise
W_tx = np.zeros((nx + 1, nt + 1))
for x in range(nx):
    for t in range(nt):
        dW = np.sqrt(delta_t * delta_x) * np.random.normal(0, 1, size=1 )
        W_tx[x + 1, t + 1] = W_tx[x, t + 1] + W_tx[x + 1, t] - W_tx[x, t] + dW[0]

# print(W_tx)

# Plot the Brownian Sheet

ts, xs = np.meshgrid(t_axis, x_axis)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
#ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
ax.set_xlabel('$ 0 \\leq t \\leq 2 $', fontsize=14)
plt.xticks([0,.5,1,1.5,2])
ax.set_ylabel('$0 \\leq x \\leq 2$', fontsize=14)
plt.yticks([0,.5,1,1.5,2])
ax.xaxis.set_pane_color((0, 0, 0, 0))
ax.yaxis.set_pane_color((0, 0, 0, 0))
ax.zaxis.set_pane_color((0, 0, 0, 0))
#ax.plot_surface(ts, xs, W_tx, rstride=20, cstride=20, cmap='autumn_r', linewidth=.5, edgecolor='black')

ax.plot_surface(ts, xs, W_tx, rstride=1, cstride=1, cmap='plasma')
ax.set_title('Brownian Sheet',fontsize=20)
plt.show()
