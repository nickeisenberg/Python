# A simulation of the 1-d SHE with vanishing boundary conditions
# u_t - (1/2)u_{xx} = u \dot{W}
# We consider the case of a linear multiplicative space-time white noise
# We use the space-time white noise expansion given in EX 4.9 - DaPrato Red Book

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Set the time and space intervals. Choose number of partitions of each.

# Time
t = .1
nt = 500
delta_t = t / nt

# Space
x = 1
nx = 15
delta_x = x / nx

# create the time and spatial axis
t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# Set the initial condition
# Insure that the vansihing boundary condition is met
def f(x):
    return np.round(np.sin(math.pi * x), 5)

# Set up a matrix defining u(t,x) = (u)_{i,j}
u = np.zeros((nx+1, nt+1), dtype=float)

# Enter initial data
u[0:,0] = f(x_axis)

# Set up space time white noise

dW = np.zeros((nx+1, nt+1))

for i in range(nx):
    for j in range(nt):
        dWij = np.sqrt(delta_t)*np.sqrt(delta_x) * np.random.normal(0, 1, size=1 )
        dW[i+1][j+1] = dWij[0]

# Set up the finite difference scheme
for j in range(nt):
    for i in range(1,nx):
        u[i,j+1] = u[i,j] + ((nx) ** 2) * (delta_t / 4) * (u[i+1,j] + u[i-1,j] - 2 * u[i,j])\
                    + 1 *  nx * u[i,j] * dW[i+1,j+1]

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

# Plot the approximate solution along with the noise

# Approximate solution
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(121, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Space', fontsize=14)
ax.plot_surface(ts, xs, u, rstride=1, cstride=1, cmap='plasma')
ax.set_title('Discretized SHE',fontsize=20)


# Noise
ax1 = fig.add_subplot(122, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax1)
# ax1.set_xlabel('$ 0 \\leq t \\leq .1 $', fontsize=14)
# ax1.set_ylabel('$0 \\leq x \\leq 1$', fontsize=14)
ax1.plot_surface(ts, xs, dW, rstride=1, cstride=1, cmap='plasma')
ax1.set_title('Space time white noise',fontsize=20)
plt.show()

plt.show()
