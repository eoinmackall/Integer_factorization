import math
import random

def PollardRho(m, s=None):
    """
    Input: an integer m, a seed s (if no seed specified, then a random seed is used)

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by implementing Pollard's rho algorithm using polynomial x^2+1 for
    recursively defined sequence. Implements Floyd's cycle finding algorithm.
    """

    #Setup
    n=abs(m)

    if n<=2:
        return (False, m)

    if s == None:
        s=random.randrange(2,n)

    #Function for computing recursive rho sequence
    def f(x):
        return (x**2 + 1) % n

    #The main algorithm for finding divisors (Floyd's cycle finding algorithm)
    x = s
    y = s
    d = 1
    i = 0

    while d == 1 and i<=1:
        x = f(x) #calculates x_i
        y = f(f(y)) #calculates x_{2i}
        d = math.gcd(x - y, n)
        if d == n:
            d=1
        if x == y:
            i+=1

    if d != 1:
        return (True, d)
    else:
        return (False, m)