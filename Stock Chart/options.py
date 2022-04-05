import yfinance as yf
import pendulum
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

tick = yf.Ticker('GME')
#print(tick.options)

opt = pd.read_csv('GME_2022_04_01.csv')

sym = opt['Symbol']
gamma = opt['Gamma']
delta = opt['Delta']
openint = opt['Open Int']

x = sym[263]
print(x)
print(x[len(x)-1] == 'P')






# rows = min(len(delta), len(openint))
#
# data = np.zeros((rows, 2))
#
# for i in range(rows):
#     if delta[i] >= -1:
#         data[i,0] = delta[i]
#     else:
#         data[i,0] = 0
#
# for i in range(rows):
#     if type(openint[i]) != 'int':
#         data[i,1] = 0
#     else:
#         data[i,1] = openint[i]
# print(delta[260])
