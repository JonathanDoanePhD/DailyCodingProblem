# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

import math
import itertools as itr

N = 4

def ANS(in_N=N):
    n = in_N + 1
    out = 0
    for i in range(n//2, n):
        out += len(list(itr.combinations(range(i), in_N - i)))
    return out

print(ANS())

# 1: (1)
# 1

# 2: (2)
# 1, 1
# 2

# 3: (3)
# 1, 1, 1
# 2, 1
# 1, 2

# 5: (8)
# 1, 1, 1, 1, 1
# 2, 1, 1, 1
# 1, 2, 1, 1
# 1, 1, 2, 1
# 1, 1, 1, 2
# 2, 2, 1
# 2, 1, 2
# 1, 2, 2

X = {1, 5, 3}

def ANS0(in_N=N, in_X=X):
    out = 0
    for i in range(in_N):
        i += 1
        L = list(itr.combinations_with_replacement(X, i))
        for l in L:
            if sum(l) == in_N:
                out += len(list(set(itr.permutations(l, i))))
            else:
                pass
    return out

print(ANS0())

# 4: (3)
# 1, 1, 1, 1
# 3, 1
# 1, 3

# 1: (1)
# 1

# 2: (1)
# 1, 1

# 3: (2)
# 1, 1, 1
# 3

# 5: (5)
# 1, 1, 1, 1, 1
# 3, 1, 1
# 1, 3, 1
# 1, 1, 3
# 5

# 6: (8)
# 1, 1, 1, 1, 1, 1
# 3, 1, 1, 1
# 1, 3, 1, 1
# 1, 1, 3, 1
# 1, 1, 1, 3
# 3, 3
# 5, 1
# 1, 5