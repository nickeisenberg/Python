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

# Set up the space-time white noise
# We first simulate K independent brownian motions

K = 25

W = np.zeros((nt + 1, K + 1), dtype=float)
for i in range(K):
    dW = np.sqrt(delta_t) * np.random.normal(0, 1, size=nt )
    W[1:,i] = np.cumsum(dW)

# Denote the space-time white noise as W_tx = Wtx
# Recall that Wtx(t, x) = SUM where SUM is the sum from Example 4.9 DaPrato

def Wtx(t, x):
    x_index = int(x / delta_x)
    t_index = int(t / delta_t)
    Bnt = W[t_index]
    sin_in = np.zeros(K + 1)
    frac = np.zeros(K + 1)
    for i in range(K + 1):
        sin_in[i] = (i + .5) * x
        frac[i] = 1 / (i + 1 / 2)
    sin = np.sin(sin_in)
    BSfrac = np.multiply(np.multiply(sin, Bnt), frac)
    sumand = math.sqrt(2 / math.pi) * BSfrac
    return np.sum(sumand)

# Store the values of Wtx in a matrix (aij) where aij = W( t_j, x_i)
# Note that a0j = 0 and ai0 = 0 from the definion of the SUM from Example 4.9

W_tx = np.zeros((nx + 1, nt + 1))

for i in range(nx + 1):
    for j in range(nt + 1):
        W_tx[i][j] = Wtx(t_axis[j], x_axis[i])

# Set up the finite difference scheme
for j in range(nt):
    for i in range(1,nx):
        u[i,j+1] = u[i,j] + ((nx) ** 2) * (delta_t / 4) * (u[i+1,j] + u[i-1,j] - 2 * u[i,j])\
                    + .01 *  nx * u[i,j] * W_tx[i,j]

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

# Plot the approximate solution along with the noise

# Approximate solution
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(121, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
# ax.set_xlabel('$ 0 \\leq t \\leq .1 $', fontsize=14)
# ax.set_ylabel('$0 \\leq x \\leq 1$', fontsize=14)
ax.plot_surface(ts, xs, u, rstride=1, cstride=1, cmap='plasma')
ax.set_title('Discretized SHE',fontsize=20)

# Noise 
ax1 = fig.add_subplot(122, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax1)
# ax1.set_xlabel('$ 0 \\leq t \\leq .1 $', fontsize=14)
# ax1.set_ylabel('$0 \\leq x \\leq 1$', fontsize=14)
ax1.plot_surface(ts, xs, W_tx, rstride=1, cstride=1, cmap='plasma')
ax1.set_title('Noise',fontsize=20)
plt.show()

plt.show()
