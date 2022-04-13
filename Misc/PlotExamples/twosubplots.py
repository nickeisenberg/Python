import numpy as np
import matplotlib.pyplot as plt

# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create two subolots side by side
f, (ax1, ax2) = plt.subplots(2, sharey=True)
ax1.plot(x, y)
ax1.set_title('ax_1 title')
ax2.scatter(x, y)
ax2.set_title('ax_2 title')

## Create two subplots stacked vertically
#f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
#ax1.plot(x, y)
#ax1.set_title('ax_1 title')
#ax2.scatter(x, y)
#ax2.set_title('ax_2 title')

plt.show()
