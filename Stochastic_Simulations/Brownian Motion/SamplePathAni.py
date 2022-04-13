# Animating a brownian sample path 

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

# create the time interval and partition 
t = 5 
n = 500 

# How many sample paths?
path_amt = 2

# Create a brownian sample path 
def bsp(t, n):
    dB = np.sqrt(t / n) * np.random.normal(0, 1, size=n)
    B = np.zeros(n+1)
    B[1:] = np.cumsum(dB)
    return(B)

# Simulate "path_amt" sample paths 
def sample_paths(i, t ,n):
    BSP = np.zeros((i, n+1))
    for k in range(i):
        BSP[k,:] = bsp(t, n) 
    return(BSP)

B_paths = sample_paths(path_amt, t, n)

# Create the animation function for the sample path
x = []
y = []
t_axis = np.linspace(0, t, n+1)

fig, ax = plt.subplots()

ax.set_xlim(0, 5.3)
ax.set_ylim(-4, 4)

line, = ax.plot(0, 0)

def anim_func(i):
    x.append(t_axis[int(i * n / t)])
    y.append(B_paths[0][int(i * n / t)])

    line.set_xdata(x)
    line.set_ydata(y)
    return line,

animation = FuncAnimation(fig, func = anim_func, \
                frames = np.linspace(0, t, n+1), interval = 3, repeat=False)

plt.show()

animation.save('BrownianPathAnim.gif', writer='imagemagick', fps=60)

# Create an animation of the first sample path
#t_axis = np.linspace(0, t, n+1)
#
#t = []
#y = []
#
#for amt in range(path_amt):
#   for i in range(n+1):
#        t.append(t_axis[i])
#        y.append(B_paths[amt][i])
#
#        plt.xlim(0,3)
#        plt.ylim(-3,3)
#
#        plt.plot(t, y)
#        plt.pause(0.0000001)

#plt.show()
