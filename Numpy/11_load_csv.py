import numpy as np
data = np.loadtxt("ChieuCaoChaVaCon.csv", delimiter=",", skiprows=1, usecols=[1, 3])
print(data)
