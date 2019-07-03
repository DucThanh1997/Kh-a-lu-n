import numpy as np


x = np.array([0, 1, 0, 1], np.uint8)
y = np.array([0, 0, 1, 1], np.uint8)

print("phép AND: ", np.bitwise_and(x, y))
print("phép OR: ", np.bitwise_or(x, y))
print("phép OR: ", np.bitwise_xor(x, y))
print("phép OR: ", np.bitwise_not(x))

