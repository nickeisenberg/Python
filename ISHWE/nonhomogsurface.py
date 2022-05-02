import numpy as np
from scipy.special import gamma, factorial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def Y_2b01(T,X,b):
    K = 200
    Y = np.zeros((n+1, n+1))
    for t in range(len(T)):
        for x in range(len(X)):
            m_i = np.zeros(K)
            for i in range(K):
                m_i[i] = (((-1) ** i) * (abs(X[x]) / (T[t] ** (b/2)))**i ) / (factorial(i) * gamma(b - ((i + 1) * (b / 2))))
                value = ((T[t] ** ((b / 2) - 1)) / 2) * m_i
                sum_i = sum(value)
            Y[x,t] = sum_i
    return(Y)

# x axis
x0 = -4
xn = 4

# partition the x axis and t axis
n = 50
x_axis = np.linspace(x0, xn, n + 1)

t = 6
t_axis = np.linspace(1, t, n + 1)

# specify b
b = .7

# Set up grid
ts, xs = np.meshgrid(t_axis, x_axis)

fig = plt.figure(figsize=(8,8))
plt.axis('off')
ax = fig.add_subplot(111, projection='3d')
fig.add_axes(ax)

ax.plot_surface(ts, xs, Y_2b01(t_axis, x_axis, b), rstride=1, cstride=1, cmap='plasma')

ax.xaxis.set_pane_color((0, 0, 0, .6))
ax.yaxis.set_pane_color((0, 0, 0, .6))
ax.zaxis.set_pane_color((0, 0, 0, .6))

ax.view_init(30, -135)
plt.show()
