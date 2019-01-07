def levenshteinDistance(firstWord: str, secondWord: str):
    '''
    >>> levenshteinDistance("kitten", "sitting")
    3
    >>> levenshteinDistance("god", "dog")
    2
    >>> levenshteinDistance("love", "love")
    0
    '''
    counter = 0

    if len(firstWord)>len(secondWord):
        for i in range(len(secondWord)):
            if firstWord[i]!=secondWord[i]:
                counter+=1
        return counter + (len(firstWord)-len(secondWord))
    else:
        for i in range(len(firstWord)):
            if firstWord[i]!=secondWord[i]:
                counter+=1
        return counter + (len(secondWord)-len(firstWord))


if __name__ == "__main__":
    import doctest
    doctest.testmod()