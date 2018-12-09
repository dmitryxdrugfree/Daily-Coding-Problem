"""
Daily Coding Problem: Problem #2 by Uber
"""
def magicProductNumArray(arrayOfNums):
    magicArray = []
    if len(arrayOfNums) > 1:
        for i in arrayOfNums:
            magicCounter = 1
            for j in arrayOfNums:
                if j!=i:
                    magicCounter *= j
            magicArray.append(magicCounter)
        return magicArray
    return arrayOfNums
        
        

def checkSolution():
    if magicProductNumArray([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]:
        print("Test 1 - OK")
    else: 
        print("Test 1 - Fail!")
        
    if magicProductNumArray([3, 2, 1]) == [2, 3, 6]:
        print("Test 2 - OK")
    else: 
        print("Test 2 - Fail!")
    
    if magicProductNumArray([2, 1]) == [1, 2]:
        print("Test 3 - OK")
    else: 
        print("Test 3 - Fail!")
    
    if magicProductNumArray([12]) == [12]:
        print("Test 4 - OK")
    else: 
        print("Test 4 - Fail!")

checkSolution()        