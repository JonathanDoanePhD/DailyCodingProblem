# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

import numpy as np
import itertools as itr

N = 5
k = 3
a = np.array([[400, 200, 400, 200, 500],
              [300, 200, 300, 200, 400],
              [300, 300, 400, 500, 300]])

sol = [1, 0, 1, 0, 2]
ans = 300 + 200 + 300 + 200 + 300

def ANS(in_array=a):
    a = in_array
    N = a.shape[1]
    k = a.shape[0]
    R = [list(range(k)) for x in range(N)]
    paths = [I for I in itr.product(*R) if (I[0]!=I[1] and I[1]!=I[2] and I[2]!=I[3] and I[3]!=I[4])]
    costs = []
    for I in paths:
        cost = 0
        for j in range(N):
            cost += a[I[j]][j]
        costs.append(cost)
    return min(costs)

A = ANS()
print(A, ans, A == ans)