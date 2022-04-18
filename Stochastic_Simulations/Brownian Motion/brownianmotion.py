#Simulating a Brownain Motion in 1-d starting at 0

import numpy as np
import matplotlib.pyplot as plt

# We consider the time interval (0,t)
# We partion the interval into 1000 pieces. P denotes the partition.

t=5
n=1000
delta_t = t/n

# For i \in P, recall that W_i - W_{i-1} ~ N(0,t/n)
# We sample 1000 samples from n(0,t/n), {dW_{i-1}}_{1 \le i \le 1000}
# We approximate W_j by W_j = W_{j-1} + dW_{j-1}
# Through iteration, W_j = dW_{0} + ... + dW_{j-1}

dW = np.sqrt(delta_t) * np.random.normal(0,1,size =n )

W = np.empty(n+1, dtype=float)
W[0] = 0
for i in range(n):
    W[i+1] = W[i] + dW[i]

# There is a bulit in formula, np.cumsum, that does what the above for loop does.
# W = Wt
# Wt = np.zeros(n+1)
# Wt[1:] = np.cumsum(dW)



# x-axis for the plot

x = np.zeros(1)
for i in range(n):
    xi = delta_t * (i+1)
    x = np.append(x,xi)

plt.plot(x,W)
plt.title('Brownian Motion')
plt.show()
