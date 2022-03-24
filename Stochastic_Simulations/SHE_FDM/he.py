# A finite-difference approx of the 1-d Heat Equation with vanishing boundary conditions
# u_t - (1/2)u_{xx} = 0

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
nx = 50
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

# Set up the finite difference scheme
for j in range(nt):
    for i in range(1,nx):
        u[i,j+1] = u[i,j] + ((nx) ** 2) * (delta_t / 4) * (u[i+1,j] + u[i-1,j] - 2 * u[i,j])

# print(u)

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

# Plot the approximate and the exact side by side

# Approximate solution
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(121, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
# ax.set_xlabel('$ 0 \\leq t \\leq .1 $', fontsize=14)
# ax.set_ylabel('$0 \\leq x \\leq 1$', fontsize=14)
ax.plot_surface(ts, xs, u, rstride=1, cstride=1, cmap='plasma')
ax.set_title('Discretized Solution',fontsize=20)
# plt.show()

# Exact Solution
def uexact(t,x):
    return np.sin(math.pi * x) * np.exp(-(t / 2) * (math.pi)**2)

uex = uexact(ts,xs)

# Plot the exact solution

# fig1 = plt.figure(figsize=(8,8))
ax1 = fig.add_subplot(122, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax1)
# ax1.set_xlabel('$ 0 \\leq t \\leq .1 $', fontsize=14)
# ax1.set_ylabel('$0 \\leq x \\leq 1$', fontsize=14)
ax1.plot_surface(ts, xs, uex, rstride=1, cstride=1, cmap='plasma')
ax1.set_title('Exact Solution',fontsize=20)
plt.show()
