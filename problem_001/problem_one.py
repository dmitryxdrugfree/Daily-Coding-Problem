# -*- coding: utf-8 -*-
"""
Daily Coding Problem: Problem #1 by Google
"""
def isTwoNumbersAddUpToK (nums, k):
    if len(nums)>1:
        for i in range(len(nums)-1):
            if nums[i] >= k:
                i+=1
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == k:
                    return True
            return False
    return False
            

def checkSolution():
    if isTwoNumbersAddUpToK([10, 15, 3, 7], 17)==True:
        print("Test 1 - OK")
    else:
        print("Test 1 - Fail!")   
    
    if isTwoNumbersAddUpToK([21, 15, 3, 7, 2], 17)==True:
        print("Test 2 - OK")
    else:
        print("Test 2 - Fail!")        
    
    if isTwoNumbersAddUpToK([3, 7, 2], 17)==False:
        print("Test 3 - OK")
    else:
        print("Test 3 - Fail!")        
   
    if isTwoNumbersAddUpToK([], 7)==False:
        print("Test 4 - OK")
    else:
        print("Test 4 - Fail!") 


checkSolution()