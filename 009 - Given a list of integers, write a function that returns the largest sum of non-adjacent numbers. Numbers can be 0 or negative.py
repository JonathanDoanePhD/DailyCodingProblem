a0 = [2, 4, 6, 2, 5] # 13
a1 = [5, 1, 1, 5] # 10

e0 = list(enumerate(a0))
e1 = list(enumerate(a1))

def Group_is_Nadj(in_list=[e0[0], e0[2], e0[4]]):
    l = in_list.copy()
    inds = [x[0] for x in l]
    check = [i for i in inds if i+1 in inds]
    # print(inds)
    # print(check)
    # print()
    return check == []

import itertools as itr






# def Non_Adj_Groups(in_list):



def ANS(in_list=a0):
    l = in_list.copy()
    e = list(enumerate(l))
    largest_nadj = (len(l)+1) // 2

    out = []
    for i in range(1, largest_nadj+1):
        check = [list(x) for x in itr.combinations(e, i)]
        for c in check:
            if Group_is_Nadj(c):
                out.append(sum([x[1] for x in c]))
            else:
                pass
    # print()
    # for o in out:
    #     print(o)
    # print()
    return max(out)



print(ANS(a1))
