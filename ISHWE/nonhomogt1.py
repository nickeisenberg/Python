import numpy as np
from scipy.special import gamma, factorial, logsumexp
import matplotlib.pyplot as plt
import mpmath as mp
from mpmath import *

#def Y_2b01(t,X,b):
#    K = 150
#    Y = np.zeros(n+1)
#    for x in range(len(X)):
#        m_i = np.zeros(K)
#        for i in range(K):
#            m_i[i] = (((-1) ** (2*i)) * (abs(X[x]) / (t ** (b/2)))** (2*i)) / \
#            (factorial(2*i) * gamma(b - (((2*i) + 1) * (b / 2))))
#            sum_i = ((t ** ((b / 2) - 1)) / 2) * m_i
#            value_x = sum(sum_i)
#        Y[x] = value_x
#    return(Y) 
#

# try using mpmath to find the sum 

def Y(i):
    if b * ((i - 1) / 2) == int(b * ((i - 1) / 2)):
        val = 0
    else:
        val = (((-1) ** (i) * (abs(x) / (t ** (b/2)))**(i)) / \
        (mp.fac(i) * mp.gamma(b * ((1 -i)/2)))) * \
        ((t ** ((b / 2) - 1)) / 2)
    return(val)

for b in [.5, .8, 1, 1.4]:
    xn = 4
    n = 500
    x_axis = np.linspace(-1 * xn, xn, n+1) 

    Yvalue = np.zeros(n + 1)
    b = b
    t = 1
    ind = 0
    for x in x_axis:
        x = x 
        Yvalue[ind] = mp.nsum(Y, [0, 200])
        ind = ind + 1
    
    plt.plot(x_axis, Yvalue, label='b = {}'.format(b))
    plt.legend(loc="upper left")


for b in [1.99]:
    # x axis
    x0 = 0
    xn = 4
    
    # partition the x axis
    n = 250
    x_axis_pos = np.linspace(x0, xn, n + 1) 
    x_axis = np.linspace(-1 * xn, xn, 2*n + 1)

    Yvalue_pos = np.zeros(n + 1)
    b = b
    t = 1
    ind = 0
    for x in x_axis_pos:
        x = x
        if ind == 0:
            Yvalue_pos[ind] = mp.nsum(Y, [0, inf])
        elif ind > 0 and mp.nsum(Y, [0, inf]) <= Yvalue_pos[ind -1] and mp.nsum(Y, [0, inf]) > 0:
            Yvalue_pos[ind] = mp.nsum(Y, [0, inf])
        else:
            Yvalue_pos[ind] = Yvalue_pos[ind -1]
        ind = ind + 1
    
    Yvalue_neg = np.flip(Yvalue_pos)
    Yvalue = np.concatenate((Yvalue_neg, Yvalue_pos[1:]))
    
    plt.plot(x_axis, Yvalue , label='b = {}'.format(b))
    plt.legend(loc="upper left")



# generate one plot
# specify b
#b = 1.45
#plt.plot(x_axis, Y_2b01(1, x_axis, b), label='b = {}'.format(b))
#plt.legend(loc="upper left")

# generate multiple plots 
#for b in [1/8, 1/2, 3/4, 1, 1.2, 1.4]:
#    plt.plot(x_axis, Y_2b01(1, x_axis, b), label='b = {}'.format(b))
#plt.legend(loc="upper left")

plt.show()
