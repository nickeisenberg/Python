import numpy as np
import matplotlib.pyplot as plt

# We use recurssion from the Euler-Maruyama method to simulate the process.
k=1
m=5
s=1

# set the initial condition
x_a=0

# set the interval (a,b) and choose the size of the partition
a = 0
b = 5
n_L = 1000
delta_L = (b-a)/n_L

#partition the interval (a,b)
P_L = np.append(np.empty(0, dtype=float),a)

for i in range(n_L):
    p_i = a + ((i+1) * delta_L)
    P_L = np.append(P_L,p_i)

# Get the noise

# increments dW
dW = np.sqrt(delta_L) * np.random.normal(0,1,size = n_L )

# Apply the recursion.

Xt = np.append(np.empty(0, dtype=float),x_a)


xi = x_a
for i in range(n_L):
    xi = xi + (k*(m-xi)*delta_L) + (s*dW[i])
    Xt = np.append(Xt,xi)

#print(dW)
#print(Xt)
# plot

plt.plot(P_L,Xt, linewidth=1)
plt.title('Ornstein-Uhlenbeck Process: \
$dX_t = \sigma dW_t +\kappa(\mu -X_t) dt$ \n \
$(a,b) =({},{})$, $X_a = {}$, $\sigma ={}$, $\kappa={}$ and $\mu = {}$'\
.format(a,b,x_a,s,k,m))
plt.show()
