# We generate a random walk with values equalt to the square root of the step size
# It is a standard result that as the step size goes to 0, that the walk will ...
# ... converge to a brownian motion.

import numpy as np 
import matplotlib.pyplot as plt

# pick the interval for the random walk 
a = 0
b = 5

# jump size is h and step size is del
d = (b-a)/100
h = np.sqrt(d)

x = np.arange(a,b+(d/2),d)
dy = np.random.choice([-h, h], len(x)-1)
y =np.append([0], np.cumsum(dy))

plt.plot(x, y)
plt.title('A random walk with jump size {} and step size {} \n number of steps = {}'.format(round(h,3), d, len(dy)))
plt.show()

