#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

t=5
n=500
delta_t = t/n
x_axis = np.linspace(0, t, n+1)
# how many paths
pamt = 2

# create an array to store the paths
X = np.zeros((pamt, n+1))

# create the paths
for i in range(pamt):
    dW = np.sqrt(delta_t) * np.random.normal(0,1,size =n )

    W = np.empty(n+1, dtype=float)
    W[0] = 0
    for j in range(n):
        W[j+1] = W[j] + dW[j]
    X[i, : ] = W

# Stochastic integral = Wt**2 / 2 - t**2 / 2
StochInt = (X**2 / 2) - (x_axis / 2)

# plot paths of the integral

for i  in range(pamt):
    plt.plot(x_axis, StochInt[i])

plt.title('Sample paths for $\int_0^t\ B_s \ d B_s$')
plt.show()
