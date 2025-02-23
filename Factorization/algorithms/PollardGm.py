import math
import random

def PollardGm(n,b=None,k=1000,tests=1):
    """
    Input: integers n>0 (to be factored), b (to be used as an exponentiation base), 
    k (factorial will be evaluated and put into the exponent of b), and t. 
    If b is None, uses t random values of b between 1 and n.

    Output: Boolean-integer pair. If n is composite, returns (True, d)
    for a divisor d of n. Otherwise, returns (False,n).

    Works by implementing Pollard's p-1 method with base b to exponent k!.
    """

    #For smaller values of k, it seems to be faster to refer directly to
    #a large integer. Here 2000 is chosen arbitrarily, checked with some
    #empirical data.

    if k<2000:

        exp = math.factorial(k)

        for i in range(tests):
            if b==None:
                b=random.randrange(2,n)
            M=pow(b,exp,n)
            d=math.gcd(M,n)
            if d!=1 and d!=n:
                return (True, d)
            b=None

    #For large values of k, we compute b^{k!} mod n
    #by successively exponentiating b mod n, i.e. x_1=b^2 mod n, x_2=x_1^3 mod n,...
    else:
        for i in range(tests):
            if b==None:
                b=random.randrange(2,n)
            M=1
            for j in range(k):
                M=(M*pow(b,j+1,n)) % n
            d=math.gcd(M,n)
            if d!=1 and d!=n:
                return (True, d)
            b=None
    return (False, n)