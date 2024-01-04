# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

# In this example, assume nodes with the same value are the exact same node objects.

# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

A = [3, 7, 8, 10]
B = [99, 1, 8, 10, 11]
ans = 8

def Successor(in_pair=[A, 0]):
    A = in_pair[0]
    i = in_pair[1]
    return A[i+1]

def ANS(in_list1=A, in_list2=B):
    A, B = in_list1, in_list2
    M, N = len(A), len(B)
    m = min(M, N)
    it = 0
    condition = A[0] != B[0]
    while condition and it <= m:
        SA, SB = Successor([A, it]), Successor([B, it])
        condition = SA != SB
        it += 1
    return A[it]

print(ANS())