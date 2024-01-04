def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# cons(a, b)(f) = f(a, b)

def CAR(a, b):
    return a

def CDR(a, b):
    return b

# print(cons(1, 2)(CDR))

def car(f):
    return f(CAR)

# print(car(cons(1, 2)))

def cdr(f):
    return f(CDR)

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))