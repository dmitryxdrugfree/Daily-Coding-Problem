"""
This problem was asked by Stripe.
"""

def returnTheLostPositiveNumber(nums):
    nums.sort()
    for i in range(len(nums)-1):
        guess = nums[i] + 1
        if guess != nums[i+1] and guess != 0:
            return guess
        
    return nums[-1]+1

def checkSolution():
    if returnTheLostPositiveNumber([3, 4, -1, 1]) == 2:
        print("Test 1 - OK")
    else: 
        print("Test 1 - Fail!")
    
    if returnTheLostPositiveNumber([1, 2, 0]) == 3:
        print("Test 2 - OK")
    else: 
        print("Test 2 - Fail!")

checkSolution()