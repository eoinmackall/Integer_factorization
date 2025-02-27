from ..math_func import IntegerRoot as introot
from ..math_func import is_square as sq
import math

def QuadraticBases(n):
    """
    Input: an integer n>0.
    Output: A boolean integer pair. Returns (True, d) for a proper divisor d,
    otherwise returns (False, n).

    Seems to be a new factorization algorithm. Works by factoring quadratic polynomials
    gotten from different representations of n in base b, for appropriate integers b.
    Seems to work well if m has many representations as x*y for x approximately 
    the same size as y.
    """

    r=introot.IntegerRootGem(n,3)
    s=introot.IntegerRootGem(n,2)

    for i in range(r+1,s):
        
        #Writing n in base i as a*i^2+b*i+c
        (q,c)=divmod(n,i)        
        (q2,b)=divmod(q,i)
        a = q2 % i
        
        #Checking whether a factorization of ax^2+bx+c produces a factor of n
        disc = b**2 - 4*a*c
        if disc > 0:
            (boo,rad)=sq.is_square(disc)
            if boo:
                if b&1 == rad&1:
                    root = (-b + rad) // 2
                    d=math.gcd(a*i-root, n)
                    if d != 1 and d !=n:
                        return (True, d)
        elif disc == 0:
            root = -b//2
            d=math.gcd(a*i-root, n)
            if d != 1 and d != n:
                return (True, d)
                        
    return (False, n)

