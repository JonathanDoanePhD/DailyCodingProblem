# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.

N = 123456789 # length of stream
S = range(N) # the stream

import random as rand
rand.seed(117)

r = rand.choice(range(N))

print(S[r])