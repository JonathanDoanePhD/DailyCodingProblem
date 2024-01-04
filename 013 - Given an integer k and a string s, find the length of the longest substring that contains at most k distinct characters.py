# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

k = 2
s = 'abcba'

def ANS(in_k=k, in_s=s):
    substrings = []
    R = range(len(in_s))
    for i in R:
        for j in R:
            substrings.append(in_s[i:j+1])
    substrings = list(set(substrings))
    # print(substrings)
    return max([len(x) for x in substrings if len(list(set(list(x)))) <= in_k])

print(ANS())