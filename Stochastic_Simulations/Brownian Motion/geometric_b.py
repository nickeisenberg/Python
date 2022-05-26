import numpy as np
import matplotlib.pyplot as plt

# How many sample paths
pamt = 3
# We use recurssion from the Euler-Maruyama method to simulate the process.
m = .001
s= .01

# set the initial condition
x_a= 5

# set the interval (a,b) and choose the size of the partition
a = 0
b = 1
n_L = 500
delta_L = (b-a)/n_L

#partition the interval (a,b)
P_L = np.linspace(a,b,n_L+1)

GB = np.zeros((pamt,n_L+1))
# Function to get the processes 
def GeoB():
    # Get the noise
    # increments dW
    dW = np.sqrt(delta_L) * np.random.normal(0,1,size = n_L )
    
    # Apply the recursion.
    
    Xt = np.append(np.empty(0, dtype=float),x_a)
    
    
    xi = x_a
    for i in range(n_L):
        xi = xi + (m*xi*delta_L) + (s*xi*dW[i])
        Xt = np.append(Xt,xi)
    return Xt

for i in range(pamt):
    GB[i,:] = GeoB()
    
#print(dW)
#print(Xt)
# plot

for i in range(pamt):
    plt.plot(P_L,GB[i], linewidth=1)
plt.title('Geometric Brownian Motion: \
$dS_t = \sigma S_t dB_t + \mu S_t dt$ \n \n \
$(a,b) =({},{})$, $X_a = {}$, $\sigma ={}$, and $\mu = {}$'.format(a,b,x_a,s,m,n_L))
plt.show()

