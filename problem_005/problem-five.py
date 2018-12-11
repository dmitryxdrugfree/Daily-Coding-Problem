def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    def first(a, b):
        return a
    return f(first)

def cdr(f):
    def last(a, b):
        return b
    return f(last)

def checkSolution():
    if car(cons(3,4)) == 3:
        print("Test 1.1 - OK")
    else: 
        print("Test 1.1 - Fail!")
    
    if cdr(cons(3,4)) == 4:
        print("Test 1.2 - OK")
    else: 
        print("Test 1.2 - Fail!")

checkSolution()