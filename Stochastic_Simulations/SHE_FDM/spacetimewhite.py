import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Time
t = 5
nt = 200
delta_t = t / nt

# Space
x = 5
nx = 200
delta_x = x / nx

# create the time and spatial axis
t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

# Set up space time white noise
dW = np.zeros((nx+1, nt+1))

for i in range(nx):
    for j in range(nt):
        dWij = np.sqrt(delta_t)*np.sqrt(delta_x) * np.random.normal(0, 1, size=1 )
        dW[i+1][j+1] = dWij[0]

# plot space time white noise 
fig = plt.figure(figsize=(8,8))
# plt.axis=('off')
ax = fig.add_subplot(111, projection='3d')
fig.add_axes(ax)

ax.xaxis.set_pane_color((0, 0, 0, .6))
ax.yaxis.set_pane_color((0, 0, 0, .6))
ax.zaxis.set_pane_color((0, 0, 0, .6))

ax.plot_surface(ts, xs, dW, rstride=1, cstride=1, cmap='plasma')

plt.title('Space-time white noise: $\\dot{W}(t,x) \\approx \\int_{t-\\delta t}^t \\int_{x - \\delta x}^x dW(s,y)$', fontsize=20)
plt.show()
