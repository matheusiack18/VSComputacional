import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 5, 10, 10, 10, 20, 20, 25, 25])
y = np.array([30, 29, 28, 33, 31, 25, 22, 20, 19])

plt.grid()
plt.scatter(x, y)
plt.show()