import numpy as np
import matplotlib.pyplot as plt

# A simulation of The Ornstein-Uhlenbeck Process, X_t
# We use Theorem2.3.7 and Theroem 11.1.1 Introduction to Stochastic Integration - Kuo
# X_t = J(t) + I(t) where J and I are defined below

# Set the drift and diffusion the coefficeint.

k=1
m=5
s=1

# set the initial condition
x_a=0

# set the interval (a,b) and choose the size of the partition
a = 0
b = 5
n_L = 1000
delta_L = np.round((b-a)/n_L ,decimals = 5)



#partition the interval (a,b) into P_L
# define to deterministic part of the solution, J, on P_L
P_L = np.append(np.empty(0, dtype=float),a)
J1 = np.empty(0, dtype=float)
J2 = np.empty(0, dtype=float)
J = np.append(np.empty(0, dtype=float),x_a)

for i in range(n_L):
    p_i = a + ((i+1) * delta_L)
    P_L = np.append(P_L,p_i)
    j_i1 = -k*(p_i-a)
    J1 = np.append(J1,j_i1)
    j_i2 = -k* (p_i - a)
    J2 = np.append(J2,j_i2)

P_L = np.round(P_L,decimals = 5)

J = np.append(J,(x_a*np.exp(J1)) - (m*np.expm1(J2)))

#make the noise
#create the variable, f, for the random part of the solution

dW = np.sqrt(delta_L) * np.random.normal(0,1,size =n_L )

f = np.empty(0, dtype=float)

for tn in P_L:
    n = int((tn-a)/delta_L)
    fn = np.empty(0, dtype=float)
    en = np.empty(0, dtype=float)
    In = np.empty(0, dtype=float)
    dWn = dW[:n]
    for ti in P_L[:n]:
        fi = -k*(tn-ti)
        fn =np.append(fn,fi)
    if tn == 0:
        en = np.append(en,0)
    else:
        en = s*np.exp(fn)
    In = en * dWn
    f=np.append(f,sum(In))

#define the process

X = J + f

#plot

plt.plot(P_L,X, linewidth = 1)
plt.title('Ornstein-Uhlenbeck Process: \
$dX_t = \sigma dW_t +\kappa(\mu -X_t) dt$ \n \
$(a,b) =({},{})$, $X_a = {}$, $\sigma ={}$, $\kappa={}$ and $\mu = {}$'\
.format(a,b,x_a,s,k,m))
plt.show()
