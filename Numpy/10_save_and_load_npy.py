import numpy as np

x = np.arange(100)


np.save("x.npy", x)

data = np.load("x.npy")
print(data)
