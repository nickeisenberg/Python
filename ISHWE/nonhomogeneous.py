import numpy as np
from scipy.special import gamma, factorial
import matplotlib.pyplot as plt

def Y_2b01(t,X,b):
    K = 200
    Y = np.zeros(n+1)
    for x in range(len(X)):
        m_i = np.zeros(K)
        for i in range(K):
            m_i[i] = (((-1) ** i) * (abs(X[x]) / (t ** (b/2)))**i ) / (factorial(i) * gamma(b - ((i + 1) * (b / 2))))
            value = ((t ** ((b / 2) - 1)) / 2) * m_i
            sum_i = sum(value)
        Y[x] = sum_i
    return(Y) 

# x axis
x0 = -4
xn = 4

# partition the x axis
n = 500
x_axis = np.linspace(x0, xn, n + 1) 

# specify b
b = 1.45

# plot
plt.plot(x_axis, Y_2b01(1, x_axis, b))
plt.show()
