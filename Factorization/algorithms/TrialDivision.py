from ..math_func import IntegerRoot as root

def TrialDivision(n,B=None):
    """
    Input: an integer n>0

    Output: Boolean-integer pair. If m is composite, returns (True, d)
    for a divisor d of m. Otherwise, returns (False,m).

    Works by dividing n by 1, 2, 3,...
    """

    if n==1 or n==2:
        return (False, n)

    if B==None:
        B=root.IntegerRootGem(n,2)
    
    for i in range(2,B):
        if n % i ==0:
            return (True,i)
    
    return (False, n)