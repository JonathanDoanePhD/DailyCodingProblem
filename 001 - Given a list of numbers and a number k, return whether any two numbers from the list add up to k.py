l = [10, 15, 3, 7]
k = 17

# max([])

# v = []
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         v.append(l[i]+l[j])

# print(v)
# print(k in v)

print(bool(max([0]+[int(k in v) for v in [[l[i]+l[j] for j in range(i+1, len(l))] for i in range(len(l))]])))

#####################################################

ans = [False]*5 + [False]*5 + [False, False, True, False, False] + [False, False, False, True, False] + [False*5]
out = []
for I, l in enumerate([[], [1], [1], [500, 40, 3], [500, 40, 3]]):
    for J, k in enumerate([0, 0, 1, 543, 541]):
        out.append(ans[I+J] == bool(max([0]+[int(k in v) for v in [[l[i]+l[j] for j in range(i+1, len(l))] for i in range(len(l))]])))

if False not in out:
    print('It works!')
else:
    print("It doesn't work...")