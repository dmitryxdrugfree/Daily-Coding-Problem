def countCharInStr(strOfChar: str):
    '''
    >>> countCharInStr("AAAABBBCCDAA")
    '4A3B2C1D2A'
    '''
    resultStr = ""
    counter = 1
    for i in range(1, len(strOfChar)):
        if strOfChar[i] == strOfChar[i-1]:
            counter += 1
        else:
            if counter >= 1:
                resultStr += str(counter) + strOfChar[i-1]
                counter = 1
    
    # i know, it's a little creepy solution
    if counter > 1:
        resultStr+= str(counter)
    resultStr += strOfChar[len(strOfChar)-1]
    
    return resultStr


if __name__ == "__main__":
    import doctest
    doctest.testmod()