# A simulation of the 1-d SHE with vanishing boundary conditions
# u_t - (1/2)u_{xx} = \lambda * u \dot{W}
# k is a multipicative constant.
# We consider the case of a linear multiplicative space-time white noise
# We use the space-time white noise expansion given in EX 4.9 - DaPrato Red Book

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import animation

# Set the time and space intervals. Choose number of partitions of each.

# Time
t = .10038
nt = 500
delta_t = t / nt

# Space
x = 1
nx = 100
delta_x = x / nx

# create the time and spatial axis
t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# choose lambda
#lbd = 1

# Set up space time white noise
dW = np.zeros((nx+1, nt+1))

for i in range(nx):
    for j in range(nt):
        dWij = np.sqrt(delta_t)*np.sqrt(delta_x) * np.random.normal(0, 1, size=1 )
        dW[i+1][j+1] = dWij[0]

# Set the initial condition
# Insure that the vansihing boundary condition is met

#def f(x):
#        return np.round(np.sin(math.pi * x), 5)

def f(arg):
        return np.round((1 / np.sqrt(.0001)) * np.exp((-1) * (np.absolute(arg - (x / 2)) ** 2) / .0002), 5)

def ulbd(lbd):
    def uheat(t, nt, delta_t, x, nx, delta_x, lbd, dW, f):
        # Set up a matrix defining u(t,x) = (u)_{i,j}
        u = np.zeros((nx+1, nt+1), dtype=float)

        # Enter initial data
        u[0:,0] = f(x_axis)

        # Set up the finite difference scheme
        for j in range(nt):
            for i in range(1,nx):
                u[i,j+1] = max(u[i,j] + ((nx) ** 2) * (delta_t / 4) * (u[i+1,j] + u[i-1,j] - 2 * u[i,j])\
                            + lbd *  nx * u[i,j] * dW[i+1,j+1], 0)
        return(u)
    # Set up the solution
    ulbd = uheat(t, nt, delta_t, x, nx, delta_x, lbd, dW, f)
    return(ulbd)

# u = ulbd(lbd)
NF = 10 
u = np.zeros((NF,nx+1, nt+1))
for i in range(NF):
    u[i,:,:] = ulbd(3 * ((i+1)/NF))

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

# Plot the approximate solution
fig = plt.figure(figsize=(8,8))
#plt.title('A finite differnece method simulation of \n \
#$u_t(t,x) - \\dfrac{{1}}{{2}} u_{{xx}}(t,x) = {} u(t,x)\\dot{{W}}(t,x)$ \n \
#$u(x,0) = \\sin(\\pi x)$'.format(lbd))
plt.axis('off')

# Approximate solution
ax = fig.add_subplot(111, projection='3d')
fig.add_axes(ax)
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Space', fontsize=14)

def animate(i):
    ax.xaxis.set_pane_color((0, 0, 0, .6))
    ax.yaxis.set_pane_color((0, 0, 0, .6))
    ax.zaxis.set_pane_color((0, 0, 0, .6))
    ax.title.set_text('A finite differnece method simulation of \n \
$u_t(t,x) - \\dfrac{{1}}{{2}} u_{{xx}}(t,x) = {} u(t,x)\\dot{{W}}(t,x)$ \n \
$u(x,0) = \\delta_0 (x)$'.format(round(3 * ((i+1) / NF), 3)))
    ax.plot_surface(ts, xs, u[i,:,:], rstride=1, cstride=1, cmap='cool')

#ax.plot_surface(ts, xs, u[4,:,:], rstride=1, cstride=1, cmap='plasma')

anim = animation.FuncAnimation(fig, animate, frames=NF)
anim.save('simulation3.gif', writer='imagemagick', fps=4)

#plt.show()
