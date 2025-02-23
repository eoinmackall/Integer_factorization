"""
Comments:
There are two functions below (IntegerRoot and IntegerRootGem) which find, for a given
pair of positive integers n and m, the largest integer b such that b^m<n.
IntegerRootGem uses a binary search by exponentiation, IntgerRoot uses a binary search
by repeated division. 

If m is small (depending on n), then IntegerRootGem tends to
perform more efficiently than IntegerRoot. On the other hand, if n and m are both large,
then IntegerRoot performs much better than IntegerRootGem.
"""

import math

def LengthOfBase(n,z):
    """
    Input: integers n,z>0.
    Output: the number of base z digits of n minus 1.
    """

    i=-1
    while n>0:
        n=n//z
        i+=1

    return i

def IntegerRoot(n, m):
    """
    Input: integer n>0, integer m>0.

    Output: largest integer b such that b^m is less or equal n.

    How it works: For each integer z between 2 and n-1, write n in
    base z. Implements a binary search to find z such that n has m
    digits in base z and m-1 digits in base z+1. 
    """

    if m==1:
        return n

    x=2
    length_x=LengthOfBase(n,2)
    if m>length_x:
        return 1
    y=n-1
    
    z=(x+y)//2

    while True:

        deg1=LengthOfBase(n,z)
        deg2=LengthOfBase(n,z+1)
            
        if deg1 >= m:
            if deg2<m:
                return z
            else:
                x=z
        else:
            y=z

        z=(x+y)//2


def IntegerRootGem(n, m):
    """
    Input: integer n>0, integer m>0.

    Output: largest integer b such that b^m is less or equal n.

    How it works: binary search by exponentiation of base b.
    """

    if m == 1:  # Handle the trivial case where m is 1
        return n

    low = 1
    high = n

    result=None
    while low <= high:
        mid = (low + high) // 2  # Integer division to avoid floating-point

        if mid**m <= n:
            result = mid  # Potential candidate, store it
            low = mid + 1  # Try higher values
        else:
            high = mid - 1  # Try lower values
    if result==None:
        result=1

    return result