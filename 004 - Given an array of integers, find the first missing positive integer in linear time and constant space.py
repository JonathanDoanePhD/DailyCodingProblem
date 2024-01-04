import numpy as np

a = np.array([[0, -1, -1.2, 2.4, 5], [-5, 10, 10.1, 10.9, 4]])
a0 = np.array([[0, -1, -1.2, -2.4, -5], [-5, -10, -10.1, -10.9, -4]])

print(max(0, int(np.max(a)//1)) + 1)