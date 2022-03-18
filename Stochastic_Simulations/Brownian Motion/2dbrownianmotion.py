#Simulating a Brownain Motion in 2-d starting at 0 

import numpy as np
import matplotlib.pyplot as plt

# We consider the time interval (0,t)
# We partion the interval into 1000 pieces. P denotes the partition.

t=1
n=1000
delta_t = t/n

# For i \in P, recall that W_i - W_{i-1} ~ N(0,t/n)
# We sample 1000 samples from n(0,t/n), {dW_{i-1}}_{1 \le i \le 1000}
# We approximate W_j by W_j = W_{j-1} + dW_{j-1}
# Through iteration, W_j = dW_{0} + ... + dW_{j-1}

dW1 = np.sqrt(delta_t) * np.random.normal(0,1,size =n )
dW2 = np.sqrt(delta_t) * np.random.normal(0,1,size =n )

# Another way to find W below. W = Wt
# Wt = np.zeros((n+1,2), dtype=float)
# for i in range(n):
#     Wt[i+1,0] = W[i,0] + dW1[i]
#     Wt[i+1,1] = W[i,1] + dW2[i]

W = np.zeros((n+1,2), dtype=float)
W[1:,0] = np.cumsum(dW1)
W[1:,1] = np.cumsum(dW2)

# x-axis for the plot

# x = np.zeros(1)
# for i in range(n):
#     xi = delta_t * (i+1)
#     x = np.append(x,xi)


plt.plot(W[:,0],W[:,1])
plt.title('2-d Brownian Motion')
plt.show()
