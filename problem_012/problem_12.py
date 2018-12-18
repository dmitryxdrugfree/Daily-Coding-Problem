
# first task: if our climb have only 1 and 2 steps
def climbToStaircase(n):
    counter = 0
    # coz it's look like fib. sequence lets inplement this 
    fib = [1,2] + [0]*n
    for i in range(2, n):
        fib[i] = fib[i-1] + fib[i-2]
        counter = fib[i]
    return counter


def test_climbToStaircase():
    t1 = 4
    a1 = 5
    print("Test 1: ", "OK!" if climbToStaircase(t1) == a1 else "Failed!")

test_climbToStaircase()
