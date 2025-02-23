import random
import math

def MillerRabin(q, a=None, tests=1):
    """
    Input: integer q (which will be tested for compositness), integer a (used as a base),
    and an integer tests (number of times to test q) 
    
    Output: boolean, integer pair. Returns (False, q) if the test determines if q is composite.
    Otherwise, returns (True, q).

    How it works: Tests if q is composite using Miller-Rabin primality test with random base
    a if a isn't specified. If the test fails, declares that q is probably prime.
    """

    #Eliminating even q    
    if q % 2 == 0:
        return (False, 2) #q is even

    #Count powers of two dividing q-1, tracked using k
    k=0
    r=-1
    m=q-1
    
    while m&1 == 0:    
        m=m>>1
        k+=1

    for run in range(tests):
        #Select base for test, if none given as input
        if a == None:
            a=random.randrange(2,q)

        s=pow(a,m,q)
        
        if (s == 1 or s == q-1):
            a=None
            continue #q is probably prime
        else:
            for i in range(k-1):
                t=s**2 % q
                if t == 1:
                    return (False, math.gcd(s-1,q)) #q is composite, returns a divisor of q
                elif t == q-1:
                    a=None
                    continue #q is probably prime
                s=t
            #Last run
            t=s**2 % q
            if t==1:
                a=None
                continue #q is probably prime
            else:
                return (False, q) #q is composite, but no divisor found

    return (True, q)