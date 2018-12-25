"""
Calculate pi by Monte-Carlo Method
"""

import math
import random

def calc_distance(x1, x2, y1, y2):
    ''' 
    Calculate distance between 2 dots 
    >>> calc_distance(1, 1, 1, 1)
    0.0
    '''
    dist = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))
    return dist

def calc_pi(n, r):
    '''
    Calculate pi-number
    >>> calc_pi(100000, 4)
    3.141
    '''
    luck = 0
    for i in range(n):
        if calc_distance(random.uniform(0, 2*r), r, random.uniform(0,2*r), r) < r:
            luck+=1
    
    pi = round(((4*luck)/n), 4)

    
    return pi
    
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)