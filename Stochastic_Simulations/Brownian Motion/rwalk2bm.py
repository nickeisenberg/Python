import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# We consider the time interval (0,t)
# We partion the interval into 1000 pieces. P denotes the partition.

t=5
n=5000
delta_t = t/n

# create the paths 
dW = np.sqrt(delta_t) * np.random.normal(0,1,size =n )
W = np.empty(n+1, dtype=float)
W[0] = 0
W[1:] = np.cumsum(dW)

# x-axis for the plot
x_axis = np.linspace(0, t, n + 1)

# we want the numbers that divide n evenly to create the approx partitions
partno = []
for i in np.arange(1, n, 1):
    if n / i == n // i:
        partno.append(i)
partno.sort(reverse=True)

# create a function that generates the approx of the brownian motion
def approxBM(j):
    plt.clf()
    size = partno[j]
    amt = n // size
    Waprx = np.zeros(amt + 1)
    x_axis_approx = np.zeros(amt + 1)
    for i in range(amt):
        Waprx[i + 1] = W[size * (i +1)]
        x_axis_approx[i + 1] = x_axis[size * (i+1)]
    plt.title('The evolution of a random walk to Brownian Motion', fontdict = {'fontsize' : 16})
    return plt.plot(x_axis_approx, Waprx)

fig = plt.figure(figsize=(8,8))
NF = len(partno)
anim = animation.FuncAnimation(fig, approxBM, frames=NF)
# anim.save('rwalk2bm.gif', writer='imagemagick', fps=5)
plt.show()

"""
# aprx = n // (10 * k)
Waprx = np.zeros(aprx + 1)
x_axis_aprx = np.zeros(aprx + 1)
for i in range(aprx):
    Waprx[i + 1] = W[int(100*(i + 1))] 
    x_axis_aprx[i + 1] = x_axis[100*(i + 1)]

plt.plot(x_axis_aprx, Waprx, marker='o')
plt.show()
"""
