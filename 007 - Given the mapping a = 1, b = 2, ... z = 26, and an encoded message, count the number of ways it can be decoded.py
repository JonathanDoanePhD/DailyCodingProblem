a = '111'

# def Letter(x):
#     x = min(25, max(0, int(x) - 1))
#     abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     return abc[x]

def Choice(x):
    x = str(x)
    check = int(x[:2])
    if check in [10, 20]:
        return [x[2:]]
    elif 11 <= check <= 26:
        return [x[1:], x[2:]]
    else:
        return [x[1:]]

def Iter(x):
    out = []
    for choice in x:
        if choice != '':
            out = out + Choice(choice)
        else:
            out = out + ['']
    return out

def Elim(x):
    x = str(x).replace(',', '')
    x = x.replace('[', '')
    x = x.replace(']', '')
    x = x.replace(' ', '')
    return x

def Count(x):
    x = Elim(x)
    return x.count("'")//2

def Done(x):
    x = Elim(x).replace("'", '')
    if x == '':
        return True
    else:
        return False

def ANS(x):
    x = Choice(x)
    done = Done(x)
    while not done:
        x = Iter(x)
        done = Done(x)
    return Count(x)

for x in [a, '1', '11', '126', '127', '107', '55', '511', '10101027']:
        print(x, ' '*(3-len(x)), ANS(x))