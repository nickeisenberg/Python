import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 3

n = 300
part = np.linspace(a,b,n+1)

dW = np.sqrt((b-a) / n) * np.random.normal(0, 1, size=n)
W = np.zeros(n+1)
W[1:] = np.cumsum(dW)

arch = np.zeros(n+1)
count = 0
for x in part: 
    arch[count] = max(( 1 * x * (3 - x) ) + (np.sqrt((b-a) / n) * np.random.normal(0,1,size=1)), 0) 
    count = count + 1


#def bumpyarch(arg):
#    return max((arg * (x - arg) ) + (3 * np.sqrt(delta_x) * np.random.normal(0,1,size=1)), 0)

plt.plot(part, arch)
plt.show()
