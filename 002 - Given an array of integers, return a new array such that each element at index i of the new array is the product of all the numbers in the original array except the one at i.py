import numpy as np

a = np.array([1, 2, 3, 4, 5])
a0 = np.array([[1, 2, 3, 4, 5], [1, 1, 1, 1, 1]])
a1 = [3, 2, 1]

def ANS(in_array=a):
    A = in_array.copy()
    s = np.shape(A)
    one_dim = len(s) == 1
    if one_dim:
        A = np.array([list(A)])
        s = (1, s[0])
    else:
        pass
    OUT = []
    for i in range(s[0]):
        out = []
        for j in range(s[1]):
            p = 1
            for I in range(s[0]):
                for J in range(s[1]):
                    if (I, J) != (i, j):
                        p = p*A[I, J]
                    else:
                        pass
            out.append(p)
        OUT.append(out.copy())
    if one_dim:
        OUT = OUT[0]
    return np.array(OUT)

print(ANS(a0))