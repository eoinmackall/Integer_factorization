"""
Some integer factorization algorithms.
"""

import is_sqrt as oth
import math
import primality as pr
import random


def TrialDivision(m,B=None):
    """
    Input: an integer n

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by dividing n by 1, 2, 3,...
    """

    n=abs(m)

    if n==0 or n==1 or n==2:
        return (False, m)

    if B==None:
        B=int((n**(1/2))//1)+1
    
    for i in range(2,B):
        if n % i ==0:
            return (True,i)
    
    return (False, m)


def ReversedTrialDivision(m):
    """
    Input: an integer n

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by dividing n by [sqrt{n}], [sqrt{n}]-1, [sqrt{n}]-2,...
    """

    n=abs(m)

    if n==0 or n==1 or n==2:
        return (False, m)

    for i in reversed(range(2,int((n**(1/2))//1)+1)):
        if n % i ==0:
            return (True,i)
    
    return (False, m)


def FermatFactorization(m):
    """
    Input: an integer n

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by checking if y^2-n is a square, incremeneting y by one each step
    """

    n=abs(m)

    if n==0 or n==1 or n==2:
        return (False, m)
    
    for i in range(int((n**(1/2))//1),(n+1)//2):
        (logic, div)=oth.isSquare(i**2-n)
        if logic:
            d=i-div
            if d != 1 and d != n:
                return (True,d)
    
    return (False, m)


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
        d = pr.EuclideanAlgorithm(x - y, n)
        if d == n:
            d=1
        if x == y:
            i+=1

    if d != 1:
        return (True, d)
    else:
        return (False, m)
    

def PollardGm(m,b=None,k=1000,t=1000):
    """
    Input: integers m (to be factored), b (to be used as an exponentiation base), 
    k (factorial will be evaluated and put into the exponent of b), and t. 
    If b is None, uses t random values of b between 1 and n.

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by implementing Pollard's p-1 method with base b to exponent k!.
    """

    n=abs(m)

    #For smaller values of k, it seems to be faster to refer directly to
    #a large integer. Here 2000 is chosen arbitrarily, checked with some
    #empirical data.
    if k<2000:
        def factorial(x):
            if x<=1:
                return 1
            else:
                j=1
                for i in range(1,x+1):
                    j*=i
                return j

        exp = factorial(k)

        if b == None:
            for i in range(t):
                b=random.randrange(1,n)
                M=pr.FastModularExp(b,exp,n)
                d=pr.EuclideanAlgorithm(M,n)
                if d !=1 and d!=n:
                    return (True, d)

        else:
            M=pr.FastModularExp(b,exp,n)
            d=pr.EuclideanAlgorithm(M,n)
            if d !=1 and d!=n:
                return (True, d)

    #For large values of k, we compute b^{k!} mod n
    #by successively exponentiating b mod n, i.e. x_1=b^2 mod n, x_2=x_1^3 mod n,...
    else:
        if b == None:
            for i in range(t):
                b=random.randrange(1,n)
                M=1
                for i in range(k):
                    M=(M*pr.FastModularExp(b,i+1,n)) % n
                d=pr.EuclideanAlgorithm(M,n)
                if d !=1 and d!=n:
                    return (True, d)
        else:
            M=1
            for i in range(k):
                M=(M*pr.FastModularExp(b,i+1,n)) % n
            d=pr.EuclideanAlgorithm(M,n)
            if d !=1 and d!=n:
                return (True, d)
    
    return (False, m)

def EllipticCurveFactorization(m,B=100,t=100,C=None,P=None):
    """
    Input: integer m (to be factored), integer B (used as a factor base),
    integer t (number of elliptic curves to use in factorization if none selected).
    Optional input C=(a,b) a pair of coefficients describing E:y^2=x^3+ax+b and
    P=(x,y) a point on E.

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).
    """

    n=abs(m)

    while True:
        if C != None:
            (a,b)=C
            (x,y)=P
            if 4*a**3+27*b**2 == 0:
                raise "Error: discriminant defined by C vanishes"
            if y**2 != x**3+a*x+b:
                raise "Error: point P not on curve defined by C"
        else:
            x=random.randrange(1,n)
            y=random.randrange(1,n)
            a=random.randrange(1,n)
            b=y**2-x**3-a*x
    
        def Ellipticgrouplaw():
            #to be written    
            return
        
        #to be written


        if C != None:
            return (False,m)

        

    return

def QuadraticBases(m):
    """
    Input: an integer m.
    Output: A boolean integer pair. Returns (True, d) for a proper divisor d,
    otherwise returns (False, m).

    Seems to be a new factorization algorithm. Works by factoring quadratic polynomials
    gotten from different representations of m in base b, for appropriate integers b.
    Seems to work well if m has many representations as x*y for x approximately 
    the same size as y.
    """
    
    finished = False
    
    n=abs(m)

    try:

        r=math.ceil(math.cbrt(n))
        s=math.floor(math.sqrt(n))
        j=0
        for i in range(r,s):

            (q,c)=divmod(n,i)
            if c == 0:
                return (True, i)
            
            (q2,b)=divmod(q,i)
            (q3,a)=divmod(q2,i)        

            if q3!=0:
                continue
            
            disc = b**2 - 4*a*c
            if disc >= 0:
                (boo,rad)=oth.isSquare(disc)
                if boo:
                    if b&1 == rad&1:
                        root = (-b + rad) // 2
                        d=pr.EuclideanAlgorithm(a*i-root, n)
                        if d != 1 and d !=n:
                            return (True, d)
            j+=1
        return (False, m)
    finally:
        if not finished:
            print("Computation ended in iteration:", j)


def ConstantBases(m):
    """
    Input: an integer m.
    Output: A boolean integer pair. Returns (True, d) for a proper divisor d,
    otherwise returns (False, m).

    Addendum to QuadraticBases(). Works by factoring quadratic polynomials
    gotten from different representations of m in base b, for appropriate integers b.
    Seems to work well if m has representations x*y for x much smaller than y.
    """
    finished = False

    n=abs(m)

    try:
        r=math.ceil(math.cbrt(n))
        s=math.floor(math.sqrt(n))
        j=0
        for i in range(r,s):
            
            (q,c)=divmod(n,i)
            if c == 0:
                return (True, i)

            d=pr.EuclideanAlgorithm(c,n)
            if d !=1 and d != n:
                return (True, d)
            j+=1
        return (False, m)
    finally:
        if not finished:
            print("Computation ended in iteration:", j)


def Factor(n):
    """
    Input: integer n
    Output: dictionary of factors of n
    """
    #to be written.
    return

    