# Good morning! Here's your coding interview problem for today.

# This problem was asked by Snapchat.

# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
#
#           3  4  5  6  7.5                       Room 1
#  0  1  2  3  4  5                               Room 2
#                    6  7  8  9 10 11 12 13 14 15 Room 2


a = [(30, 75), (0, 50), (60, 150)]
A = 2

import networkx as nx
# An idea I had was to turn the time intervals into nodes/vertices of a graph, and connect two nodes with an edge if they intersected
# I would then look for the largest complete subgraph (Kn for the largest n) - this would force at least n rooms
# The challenge was proving that n would ultimately be the minimum number of rooms - I did not want to use too much time on it
# Instead, I completed my initial thought of sorting the rooms and periodically booking/opening up rooms as time progressed

def Intersects(in_v=a[0], in_u=a[1]):
    v, u = in_v, in_u
    a, b, c, d = v + u
    if c <= a <= d:
        return True
    elif c <= b <= d:
        return True
    elif a <= c <= b:
        return True
    elif a <= d <= b:
        return True
    else:
        return False

def ANS(in_ints=a):
    a = in_ints
    a.sort()
    rooms = 0
    for i, v in enumerate(a):
        if i == 0:
            rooms += 1
        else:
            avoid = [j for j in range(i) if Intersects(v, a[j])]
            if rooms == len(avoid):
                rooms += 1
            else:
                pass
    return rooms

ans = ANS()
print()
print('My Answer:', ans)
print('   Answer:', A)
print()
print(*['It works!' if ans == A else 'Keep trying!'])
print()
print()