# We generate a random walk with values equalt to the square root of the step size
# It is a standard result that as the step size goes to 0, that the walk will ...
# ... converge to a brownian motion.

import numpy as np 
import matplotlib.pyplot as plt

# pick the interval for the random walk 
a = 0
b = 5

# state how many paths you want to plot
pamt = 2

# jump size is h and step size is del
d = (b-a)/70
h = np.sqrt(d)

# create array to store the paths
x_axis = np.arange(a,b+(d/2),d)
X = np.zeros((pamt, len(x_axis))) 

for i in range(pamt):
    dy = np.random.choice([-h, h], len(x_axis)-1)
    y =np.append([0], np.cumsum(dy))
    X[i, : ] = y

for i in range(pamt):
    plt.plot(x_axis, X[i], marker='o')

plt.title('{} sample paths of a random walk \n jump size = {} and step size = {} \n number of steps = {}'.format(pamt, round(h,3), d, len(dy)))
plt.show()

