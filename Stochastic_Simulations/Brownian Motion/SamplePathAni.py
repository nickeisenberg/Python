# Animating a brownian sample path 

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

# create the time interval and partition 
t = 4 
n = 500 

# How many sample paths?
path_amt = 3

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
#x1 = []
#y1 = []
#t_axis = np.linspace(0, t, n+1)
#
#fig, ax = plt.subplots()
#
#ax.set_xlim(0, 4.3)
#ax.set_ylim(-2.5, 2.5)
#
#line, = ax.plot(0, 0, linewidth=1)

# Attempt to create two animations on the same plot
x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

t_axis = np.linspace(0, t, n+1)

fig, ax = plt.subplots()

ax.set_xlim(0, 4.3)
ax.set_ylim(-3, 3)

line1, = ax.plot(0, 0, linewidth=1)
line2, = ax.plot(0, 0, linewidth=1)
line3, = ax.plot(0, 0, linewidth=1)

def anim_func(i):
    x1.append(t_axis[int(i * n / t)])
    y1.append(B_paths[0][int(i * n / t)])
    
    x2.append(t_axis[int(i * n / t)])
    y2.append(B_paths[1][int(i * n / t)])

    x3.append(t_axis[int(i * n / t)])
    y3.append(B_paths[2][int(i * n / t)])

    line1.set_xdata(x1)
    line1.set_ydata(y1)
    
    line2.set_xdata(x2)
    line2.set_ydata(y2)
    
    line3.set_xdata(x3)
    line3.set_ydata(y3)
    return line1, line2, line3

animation = FuncAnimation(fig, func = anim_func, \
                frames = np.linspace(0, t, n+1), interval = 5, repeat=False)

plt.title('Sample Paths of Brownian Motion')
plt.show()
#########

#def anim_func(i):
#    x1.append(t_axis[int(i * n / t)])
#    y1.append(B_paths[0][int(i * n / t)])
#
#    line.set_xdata(x1)
#    line.set_ydata(y1)
#    return line,
#
#animation = FuncAnimation(fig, func = anim_func, \
#                frames = np.linspace(0, t, n+1), interval = 3, repeat=False)
#
#plt.show()

#animation.save('BrownianPathAnim.gif', writer='imagemagick', fps=20)

# Bad Way to do the animation
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
