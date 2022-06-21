import numpy as np
from scipy.special import gamma, factorial
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
import mpmath as mp
from mpmath import *

def Y(i):
    if b * ((i - 1) / 2) == int(b * ((i - 1) / 2)):
        val = 0
    else:
        val = (((-1) ** (i) * (abs(x) / (t ** (b/2)))**(i)) / \
        (mp.fac(i) * mp.gamma(b * ((1 -i)/2)))) * \
        ((t ** ((b / 2) - 1)) / 2)
    return(val)

# -----------------------
# x axis
x0 = 0
xn = 4

# partition the x axis
n = 25
x_axis_pos = np.linspace(x0, xn, n + 1) 
x_axis = np.linspace(-1 * xn, xn, 2*n + 1)

#t = .05
nt = 50
t_axis = np.linspace(1, 4, nt + 1)

b = .5
Yt = np.zeros((nt + 1, 2 * n + 1))
ind_t = 0
# ------------------------

# -----------------------
# for b <= 1.5 
for t in t_axis:
    ind_x = 0
    Yvalue_pos = np.zeros(n + 1)
    for x in x_axis_pos:
        Yvalue_pos[ind_x] = mp.nsum(Y, [0, 200])
        ind_x = ind_x + 1
    Yvalue_neg = np.flip(Yvalue_pos)
    Yvalue = np.concatenate((Yvalue_neg, Yvalue_pos[1:]))
    Yt[ind_t, : ] = Yvalue
    ind_t = ind_t + 1
# ------------------------

# ------------------------
## for b > 1.8. I dont think this works well for 1.5 < b < 1.8 
#for t in t_axis: 
#    ind_x = 0
#    Yvalue_pos = np.zeros(n + 1)
#    for x in x_axis_pos:
#        x = x
#        if ind_x == 0:
#            Yvalue_pos[ind_x] = mp.nsum(Y, [0, ind_x])
#        elif ind_x > 0 and mp.nsum(Y, [0, inf]) <= Yvalue_pos[ind_x -1] and mp.nsum(Y, [0, inf]) > 0:
#            Yvalue_pos[ind_x] = mp.nsum(Y, [0, inf])
#        else:
#            Yvalue_pos[ind_x] = Yvalue_pos[ind_x -1]
#        ind_x = ind_x + 1
#
#    Yvalue_neg = np.flip(Yvalue_pos)
#    Yvalue = np.concatenate((Yvalue_neg, Yvalue_pos[1:]))
#    Yt[ind_t, : ] = Yvalue
#    ind_t = ind_t + 1
# --------------------------

# plot
xs, ts = np.meshgrid(x_axis, t_axis)

fig = plt.figure(figsize=(8,8))
plt.axis('off')
ax = fig.add_subplot(111, projection='3d')
fig.add_axes(ax)

ax.plot_surface(xs, ts, Yt, rstride=3, cstride=3, cmap='autumn_r', linewidth=0.5, edgecolors='black')

ax.xaxis.set_pane_color((0, 0, 0, 0))
ax.yaxis.set_pane_color((0, 0, 0, 0))
ax.zaxis.set_pane_color((0, 0, 0, 0))

ax.view_init(33, -55)
plt.show()
