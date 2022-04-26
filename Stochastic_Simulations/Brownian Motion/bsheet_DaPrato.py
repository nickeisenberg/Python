# Simulation of a Brownian Sheet for 0 < x < pi and t > 0.
# We define the Brownian Sheet using Example 4.9 Daprato - Stoch Eq in Inf Dim
# We must only consider 0 < x < pi due to Example 4.9 DaPrato
# We may choose to divide time into nt pieces and space into nx pieces

import numpy as np
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d.axes3d import Axes3D

# Define constants.

t = 5
x = math.pi
nx = 400
nt = 400
delta_t = t / nt
delta_x = x / nx

# K will denote the upper limit of sumation from Example 4.9 DaPrato

K = 100

# Generate K + 1 Brownian Motions simulations.
# Simulate nt + 1 points: W(t_0) = 0, W(t_1), ..., W(t_k), ..., W(t_n).

W = np.zeros((nt + 1, K + 1), dtype=float)
for i in range(K+1):
    dW = np.sqrt(delta_t) * np.random.normal(0, 1 , size=nt )
    W[1:,i] = np.cumsum(dW)


# t-axis and x-axis for the plot

t_axis = np.linspace(0.0, t, nt + 1)
x_axis = np.linspace(0.0, x, nx + 1)

# Write a function Wtx(t, x) = SUM where SUM is the sum from Example 4.9 DaPrato

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

# Store the values a matrix (aij) where aij = W( t_j, x_i)
# Note that a0j = 0 and ai0 = 0 from the definion of the SUM from Example 4.9

W_tx = np.zeros((nx + 1, nt + 1))

for i in range(nx + 1):
    for j in range(nt + 1):
        W_tx[i][j] = Wtx(t_axis[j], x_axis[i])

# Turn the 2d matrix into a 3d surface

ts, xs = np.meshgrid(t_axis, x_axis)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
#ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
ax.set_xlabel('$ 0 \\leq t \\leq {} $'.format(t), fontsize=14)
ax.set_ylabel('$0 \\leq x \\leq \\pi$', fontsize=14)
ax.plot_surface(ts, xs, W_tx, rstride=1, cstride=1, cmap='plasma')
ax.set_title('Brownian Sheet: $W(t,x) \\approx \\sum_{{i=0}}^{{{}}}$\
    $\\dfrac{{\\beta_i(t)}}{{i + \\frac{{1}}{{2}} }}\
     \\sqrt{{ \\dfrac{{2}}{{\\pi}} }} \\sin\\left[ \\left(i+ \\dfrac{{1}}{{2}} \\right) x \\right]$'\
     .format(K),fontsize=20)
plt.show()
