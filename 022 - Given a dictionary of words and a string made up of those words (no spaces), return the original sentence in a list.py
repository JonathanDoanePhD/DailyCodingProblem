# Good morning! Here's your coding interview problem for today.

# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

a0 = ['quick', 'brown', 'the', 'fox', 'their']
s0 = "theirquickbrownfox"
A0 = ['their', 'quick', 'brown', 'fox']

a00 = ['quick', 'brown', 'the', 'fox']
s00 = "thequickbrownfox"
A00 = ['the', 'quick', 'brown', 'fox']

a1 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
s1 = "bedbathandbeyond"
A1 = ['bed', 'bath', 'and', 'beyond'] # or ['bedbath', 'and', 'beyond']


# string: theirquickbrownfox
# 
#       the: irquickbrownfox  FAILS
#       their: quickbrownfox  HAS quick
#       theirquick: brownfox  HAS brown
#       theirquickbrown: fox  HAS fox
#       theirquickbrownfox:   PASSES!

def ANS(in_list=a0, in_string=s0):
    a = in_list
    s = in_string
    a = [x for x in a if x in s]
    ls = len(s)
    making_s = [x for x in a if s.split(x)[0] == '']
    tracker = making_s
    condition = s not in making_s
    it = 0
    print()
    while condition:
        it += 1
        print(f'{it}.', 'tracker:', tracker)
        for i, tx in enumerate(making_s.copy()):
            ts = s[len(tx):]
            m_s = [x for x in a if ts.split(x)[0] == '']
            if m_s == []:
                tracker.remove(tx)
            else:
                tracker += m_s
            making_s = [tx + x for x in m_s]
        condition = s not in making_s
    return tracker


ans = ANS()
print()
print('My Answer:', ans)
print('   Answer:', A0)
print()
print(*['It works!' if ans == A0 else 'Keep trying!'])
print()
print()