"""
daily coding problem 18
"""

def maxInSubArray(numbers, k):
    ''' 
    >>> maxInSubArray([10, 5, 2, 7, 8, 7], 3)
    [10, 7, 8, 8]
    >>> maxInSubArray([10, 5, 2, 7, 8, 7], 4)
    [10, 8, 8]
    >>> maxInSubArray([10, 5, 2, 7, 8, 7], 5)
    [10, 8]
    >>> maxInSubArray([10, 5, 2, 7, 8, 7], 2)
    [10, 5, 7, 8, 8]
    '''
    counter = 0
    while k!=len(numbers)+1:
        numbers[counter] = max(numbers[counter:k])
        k+=1
        counter+=1
    return numbers[:counter]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)