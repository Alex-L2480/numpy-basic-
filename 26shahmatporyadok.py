import numpy as np
x = np.zeros((6, 6))
x[::2, 1::2] = 1
x[1::2, ::2] = 1
print(x)