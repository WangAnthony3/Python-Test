import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi*2, np.pi*2, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()