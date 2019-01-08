def calculateMedian(nums: list):
    '''
    >>> calculateMedian([1, 3, 2, 5, 4])
    3
    >>> calculateMedian([1, 3, 2, 5])
    2.5
    >>> calculateMedian([2, 1])
    1.5
    '''
    length = len(nums)
    nums = sorted(nums)

    if length%2 != 0:
        return nums[int(length/2)]
    else:
        return (nums[int(length/2)] + nums[int(length/2) - 1])/2


def seqMedian(nums: list):
    '''
    >>> seqMedian([2, 1, 5, 7, 2, 0, 5])
    2
    1.5
    2
    3.5
    2
    2.0
    2
    '''
    tList = list()

    for i in nums:
        tList.append(i)
        print(calculateMedian(tList))    


if __name__ == "__main__":
    import doctest
    doctest.testmod()