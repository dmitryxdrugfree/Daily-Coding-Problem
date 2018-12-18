
# first task: if our climb have only 1 and 2 steps
def climbToStaircase_1(n):
    counter = 0
    # coz it's look like fib. sequence lets inplement this 
    # f(n) = f(n - 1) + f(n - 2)
    fib = [1,2] + [0]*n
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
        counter = fib[i]
    return counter


# second task: if our climb have 1, 3 and 5 steps
def climbToStaircase_2(n):
    X = [1,3,5]
    # f(n) = f(n - 1) + f(n - 3) + f(n - 5)    
    unfib = [1] + [0]*n
    for i in range(n+1):
        unfib[i] += sum(unfib[i - x] for x in X if i - x > 0)
        unfib[i] += 1 if i in X else 0
    return unfib[-1] 


def test_climbToStaircase():
    t1 = 4
    a1 = 5
    print("Test 1: ", "OK!" if climbToStaircase_1(t1) == a1 else "Failed!")
    t2 = 6
    a2 = 8
    print("Test 2: ", "OK!" if climbToStaircase_2(t2) == a2 else "Failed!")

test_climbToStaircase()
