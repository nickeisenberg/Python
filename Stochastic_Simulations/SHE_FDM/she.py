# A simulation of the 1-d SHE with vanishing boundary conditions
# u_t - (1/2)u_{xx} = \lambda * u \dot{W}
# \lambda is a multipicative constant.
# We consider the case of a linear multiplicative space-time white noise
# We simulate the space-time white through a recursive scheme inspired by Walsh

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Set the time and space intervals. Choose number of partitions of each.

# Time
t = .2
nt = 5000
delta_t = t / nt

# Space
x = 3
nx = 200
delta_x = x / nx

# create the time and spatial axis
t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# choose lambda
lbd = 0

# Set up space time white noise
dW = np.zeros((nx+1, nt+1))

np.random.seed(3)
for i in range(nx):
    for j in range(nt):
        dWij = np.sqrt(delta_t)*np.sqrt(delta_x) * np.random.normal(0, 1, size=1 )
        dW[i+1][j+1] = dWij[0]

# Set the initial condition
# Insure that the vansihing boundary condition is met

#def f(x):
#        return np.round(np.sin(math.pi * x), 5)

def delta(arg):
    return np.round((1 / np.sqrt(.0001)) * np.exp((-1) * (np.absolute(arg - (x / 2)) ** 2) / .0002), 5)

####### bumpy arches
bumpyarch = np.zeros(nx + 1)
count = 0
for xi in x_axis:
    bumpyarch[count] =  max((np.sin((4*math.pi / 3) * (xi - (3 / 8)  ))+1) + (3*np.sqrt(delta_x) * np.random.normal(0,1,size=1)), 0)
    count = count + 1


def uheat(t, nt, delta_t, x, nx, delta_x, lbd, dW, f):
    # Set up a matrix defining u(x,t) = (u)_{i,j}
    u = np.zeros((nx+1, nt+1), dtype=float)

    # Enter initial data
    u[0:,0] = f

    # Set up the finite difference scheme. 
    # delta_t/4 should just be delta_t but the /4 helps with convergence.
    for j in range(nt):
        for i in range(1,nx):
            u[i,j+1] = max(u[i,j] + ((nx) ** 2) * (delta_t /4) * (u[i+1,j] + u[i-1,j] - 2 * u[i,j])\
                        + lbd *  nx * u[i,j] * dW[i+1,j+1], 0)
    return(u)
#######

#def uheat(t, nt, delta_t, x, nx, delta_x, lbd, dW, f):
#    # Set up a matrix defining u(x,t) = (u)_{i,j}
#    u = np.zeros((nx+1, nt+1), dtype=float)
#
#    # Enter initial data
#    u[0:,0] = f(x_axis)
#
#    # Set up the finite difference scheme. 
#    # delta_t/4 should just be delta_t but the /4 helps with convergence.
#    for j in range(nt):
#        for i in range(1,nx):
#            u[i,j+1] = max(u[i,j] + ((nx) ** 2) * (delta_t /4) * (u[i+1,j] + u[i-1,j] - 2 * u[i,j])\
#                        + lbd *  nx * u[i,j] * dW[i+1,j+1], 0)
#    return(u)

# Set up the solution
u = uheat(t, nt, delta_t, x, nx, delta_x, lbd, dW, bumpyarch)

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

# Plot the approximate solution along with the noise
fig = plt.figure(figsize=(8,8))

#plt.title('$u_t(t,x) - \\dfrac{{1}}{{2}} u_{{xx}}(t,x) = {} u(t,x)\\dot{{W}}(t,x)$ \n \
#$u(x,0) = \\delta_0(x)$'.format(lbd))

plt.title('$u_t(t,x) - \\dfrac{{1}}{{2}} u_{{xx}}(t,x) = {} u(t,x)\\dot{{W}}(t,x)$ \n \
$u(x,0) \\approx \\delta_0(x)$'.format(lbd), fontsize=20)

#plt.title('$u_t(t,x) - \\dfrac{{1}}{{2}} u_{{xx}}(t,x) = 0$ \n \
#$u(x,0) \\approx \\delta_0(x)$'.format(lbd), fontsize=20)

plt.axis('off')

# Approximate solution
ax = fig.add_subplot(111, projection='3d')
# ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
ax.set_xlabel('Time', fontsize=14)
ax.set_xticks([0, t / 2, t])
ax.set_ylabel('Space', fontsize=14)
ax.set_yticks([0, x / 2, x])
#fig.set_facecolor('xkcd:black')
#ax.set_facecolor('xkcd:black')
#ax.w_xaxis.line.set_color('white')
#ax.w_yaxis.line.set_color('white')
#ax.w_zaxis.line.set_color('white')
#ax.w_zaxis.line.set_color('white')
#ax.xaxis.label.set_color('white')
#ax.yaxis.label.set_color('white')
#ax.zaxis.label.set_color('white')
#ax.tick_params(axis='x', colors='white')  
#ax.tick_params(axis='y', colors='white') 
#ax.tick_params(axis='z', colors='white')

# See https://www.rapidtables.com/web/color/RGB_Color.html for color numbers
ax.xaxis.set_pane_color((0, 0, 0, 0))
ax.yaxis.set_pane_color((0, 0, 0, 0))
ax.zaxis.set_pane_color((0, 0, 0, 0))

ax.plot_surface(ts, xs, u, rstride=1, cstride=1, cmap='viridis')
#ax.set_title('$u(t,x)$',fontsize=20)

# # Noise
# ax1 = fig.add_subplot(122, projection='3d')
# # ax = Axes3D(fig, auto_add_to_figure=False)
# fig.add_axes(ax1)
# # ax1.set_xlabel('Time', fontsize=14)
# # ax1.set_ylabel('Space', fontsize=14)
# ax1.plot_surface(ts, xs, dW, rstride=1, cstride=1, cmap='plasma')
# ax1.set_title('Space time white noise',fontsize=20)

plt.show()
