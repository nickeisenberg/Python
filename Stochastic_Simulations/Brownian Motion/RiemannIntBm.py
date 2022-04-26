# Calculate the Riemann integral of Brownian Motion

import numpy as np
import matplotlib.pyplot as plt

# specify interval 
a = 0
b = 5

# specify partition number and size
n = 5000
delta = (b - a) / n

# partition (a,b)
part = np.linspace(a, b, n+1)

# how many paths 
pamt = 5

# brownian motion 
B = np.zeros((pamt, n + 1))
for i in range(pamt):
    dB = np.sqrt((b - a) / n) * np.random.normal(0, 1, size=n)
    B[i,1:] = np.cumsum(dB)

# calculate the riemann sums
I_t = np.zeros((pamt, n + 1))
for i in range(pamt):
    I_t[i,:] = delta * np.cumsum(B[i,:])

# plot
for i in range(pamt):
    plt.plot(part, I_t[i,:])
plt.title('{} sample paths of $\int_0^t\; B_s \; d_s = t  B_t - \int_0^t \; s \; dB_s$'.format(pamt))
plt.show()
