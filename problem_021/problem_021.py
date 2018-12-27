def findRequiredNumberOfRoom(lectures_intervals):
    '''
    >>> findRequiredNumberOfRoom([(30, 75), (0, 50), (60, 150)])
    2
    >>> findRequiredNumberOfRoom([(10, 25), (0, 50), (30, 70), (60, 120)])
    2
    >>> findRequiredNumberOfRoom([(0, 25), (0, 50), (0, 40), (30, 60)])
    3
    '''
    counter_of_classroom = 1
    lectures_intervals = sorted(lectures_intervals)

    lection_start = [i[0] for i in lectures_intervals]
    lection_end = [i[1] for i in lectures_intervals]
    
    i = 1; j = 0

    while (i < len(lectures_intervals)):
        # overlap
        if (lection_start[i] < lection_end[j]):
            counter_of_classroom += 1
            i+=1
        # free classroom 
        else:
            counter_of_classroom -= 1
            j+=1

    return counter_of_classroom


if __name__ == "__main__":
    import doctest
    doctest.testmod()