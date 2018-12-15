def findMaxSumOfNonAdjacentNumbers(numbers):
    pass

def test_solution():
    t1 = [2, 4, 6, 2, 5]
    t2 = [5, 1, 1, 5]
    print("Test 1:", "OK!" if findMaxSumOfNonAdjacentNumbers(t1) == 13 else "Failed!")
    print("Test 2:", "OK!" if findMaxSumOfNonAdjacentNumbers(t2) == 10 else "Failed!")

test_solution()