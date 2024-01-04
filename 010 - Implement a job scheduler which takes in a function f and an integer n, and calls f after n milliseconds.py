import time

def f(x):
    return x**2

n = 1000
x = 4


def ANS(in_f=f, in_n=n):
    time.sleep(in_n/1000)
    return in_f


print(ANS()(x))