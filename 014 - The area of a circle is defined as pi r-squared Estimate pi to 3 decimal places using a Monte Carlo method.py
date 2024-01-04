# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2.

# pi(x^2 + y^2) = pi r^2 = A
# If (x^2 + y^2)=1, r=1 and then pi = A
# So let's approximate the area of the unit circle

def Approx(in_grid=1):
    """Grid from 0 to in_grid length
    >>>Approx(1)
    0
    >>>Approx(2)
    1
    >>>Approx(5)
    2.08
    >>>Approx(10)
    2.68"""
    g = 1/in_grid #length of grid square
    G = [(k+1)*g for k in range(in_grid)] # right-most x-coordinates
    count = 0
    for i in range(in_grid-1):
        for j in range(in_grid-1):
            if G[i]**2 + G[j]**2 <= 1:
                count += 1
                # print(i, j)
            else:
                pass
    a = g**2 # area of grid square
    return a*(count+in_grid)*4

def ANS():
    it = 1
    est0 = Approx(it)
    est1 = Approx(it+1)
    str0 = str(est0) + '0'*10
    str1 = str(est1) + '0'*10
    s0a, s0b = str0.split('.')
    s1a, s1b = str1.split('.')
    condition = s0a != s1a or s0b[:6] != s1b[:6]
    while condition:
        # print(it)
        it += 1
        s0a, s0b = s1a, s1b
        est1 = Approx(it+1)
        if it % 10 == 0:
            print(est1)
        else:
            pass
        str1 = str(est1) + '0'*10
        s1a, s1b = str1.split('.')
        condition = s0a != s1a or s0b[:6] != s1b[:6]
    # print()
    # print('Condition met with:')
    # print(s0a + '.' + s0b)
    # print(str1)
    # print()
    return round(est1, 3)

# print(ANS())

import random as rand

# Let's fill [0, 1] \times [0, 1] with random dots, then tally them up in the circle vs outside

rand.seed(117)

X = [rand.random() for i in range(1000)]
Y = [rand.random() for i in range(1000)]

def Approx0(in_X=X, in_Y=Y, in_in=0, in_out=0):
    in_count = in_in
    out_count = in_out
    tot = in_count + out_count
    for i, x in enumerate(in_X[tot:]):
        if x**2 + in_Y[tot:][i]**2 <= 1:
            in_count += 1
        else:
            out_count += 1
    tot = in_count + out_count
    return [(in_count / tot)*4, in_count, out_count]


def ANS0(in_X=X, in_Y=Y):
    it = 1
    X0 = in_X.copy()
    Y0 = in_Y.copy()
    X1 = X0 + [rand.random() for i in range(1000)]
    Y1 = Y0 + [rand.random() for i in range(1000)]
    est0, I0, O0 = Approx0(X0, Y0)
    est1, I1, O1 = Approx0(X1, Y1, I0, O0)
    str0 = str(est0) + '0'*10
    str1 = str(est1) + '0'*10
    s0a, s0b = str0.split('.')
    s1a, s1b = str1.split('.')
    n = 5
    condition = s0a != s1a or s0b[:n] != s1b[:n]
    while condition:
        # print(it)
        it += 1
        s0a, s0b = s1a, s1b
        I0, O0 = I1, O1
        X1 = X1 + [rand.random() for i in range(1000)]
        Y1 = Y1 + [rand.random() for i in range(1000)]
        est1, I1, O1 = Approx0(X1, Y1, I0, O0)
        # print(est1)
        # if it % 100 == 0:
        #     print(est1)
        # else:
        #     pass
        str1 = str(est1) + '0'*10
        s1a, s1b = str1.split('.')
        condition = s0a != s1a or s0b[:n] != s1b[:n]
    # print()
    # print('Condition met with:')
    # print(s0a + '.' + s0b)
    # print(str1)
    # print()
    return est1

ANSs = []
seeds = range(100)
N = len(seeds)
for i, s in enumerate(seeds):
# enumerate([117, 4, 55, 7, 11, 64, 416, 16, 9, 10]):
    rand.seed(s)
    Xs = [rand.random() for i in range(1000)]
    Ys = [rand.random() for i in range(1000)]
    A = ANS0(Xs, Ys)
    print(f'{i+1} of {N}: {A}')
    ANSs.append(A)
print()
mean = sum(ANSs)/N
print(f'Approximation: {mean}')
print()
print(round(mean, 3))
print()