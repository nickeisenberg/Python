# A simulation of a Brownian sheet though theory of Walsh

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Set the time and space intervals. Choose number of partitions of each.

# Time
t = 5
nt = 50
delta_t = t / nt

# Space
x = 5
nx = 50
delta_x = x / nx

# create the time and spatial axis
t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# Create the Brownian sheet noise
W_tx = np.zeros((nx + 1, nt + 1))
for x in range(nx):
    for t in range(nt):
        dW = np.random.normal(0, delta_t * delta_x, size=1 )
        W_tx[x + 1, t + 1] = W_tx[x, t + 1] + W_tx[x + 1, t] - W_tx[x, t] + dW[0]

# print(W_tx)

# Plot the Brownian Sheet
ts, xs = np.meshgrid(t_axis, x_axis)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
#ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
# ax.set_xlabel('$ 0 \\leq t \\leq {} $'.format(t), fontsize=14)
# ax.set_ylabel('$0 \\leq x \\leq \\pi$', fontsize=14)
ax.plot_surface(ts, xs, W_tx, rstride=1, cstride=1, cmap='plasma')
ax.set_title('Brownian Sheet',fontsize=20)
plt.show()