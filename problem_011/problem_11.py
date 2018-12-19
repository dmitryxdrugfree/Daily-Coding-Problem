"""
Daily Coding Problem: Problem #11 
"""

def findPrefixInStr(listOfStrings, prefix):
    listOfStrings = list(listOfStrings.split())
    return [word for word in listOfStrings if prefix == word[:len(prefix)] ]
     

def test_findPrefixInStr():
    t11 = 'dog deer deal'; t12 = 'de'
    a1 = ['deer', 'deal']
    print("Test 1 is", "Ok!" if findPrefixInStr(t11, t12)==a1 else "failed!")
    
    t21 = 'french furr franko ferrari pofrance weed'; t22 = 'fr'
    a1 = ['french', 'franko']
    print("Test 2 is", "Ok!" if findPrefixInStr(t21, t22)==a1 else "failed!")

test_findPrefixInStr()