# Animating a brownian sample path 

import numpy as np
import matplotlib.pyplot as plt 

# create the time interval and partition 
t = 1
n = 1000
delta_t = t / n

# Create a brownian sample path 
def bsp(t, n):
    dB = np.sqrt(t / n) * np.random.normal(0, 1, size=n)
    B = np.zeros(n+1)
    B[1:] = np.cumsum(dB)
    return(B)

# Simulate "i" sample paths 
def sample_paths(i, t ,n):
    BSP = np.zeros((i, n+1))
    for k in range(i):
        BSP[i,:] = bsp(t, n) 
    return(BSP)


