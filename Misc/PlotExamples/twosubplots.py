import numpy as np
import matplotlib.pyplot as plt

# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

## Create two subolots side by side
#f, (ax1, ax2) = plt.subplots(2, sharey=True)
#ax1.plot(x, y)
#ax1.set_title('ax_1 title')
#ax2.scatter(x, y)
#ax2.set_title('ax_2 title')

# Another method 
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(x,y)
ax2.scatter(x,y)

## Good example illustrationg how to use fig.add_subplot()
#fig = plt.figure()
#fig.add_subplot(221)   #top left
#fig.add_subplot(222)   #top right
#fig.add_subplot(223)   #bottom left
#fig.add_subplot(224)   #bottom right
#plt.show()

## Create two subplots stacked vertically
#f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
#ax1.plot(x, y)
#ax1.set_title('ax_1 title')
#ax2.scatter(x, y)
#ax2.set_title('ax_2 title')

plt.show()
