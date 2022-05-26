#Simulating a Brownain Motion in 1-d starting at 0

import numpy as np
import matplotlib.pyplot as plt

# We consider the time interval (0,t)
# We partion the interval into 1000 pieces. P denotes the partition.

t=5
n=1000
delta_t = t/n

# how many paths
pamt = 100

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

# There is a bulit in formula, np.cumsum, that does what the above for loop does.
# W = Wt
# Wt = np.zeros(n+1)
# Wt[1:] = np.cumsum(dW)



# x-axis for the plot
x = np.linspace(0, t, n + 1)

# plot the paths
for i in range(pamt):
    plt.plot(x,X[i])

plt.title('Brownian Motion')
plt.show()
