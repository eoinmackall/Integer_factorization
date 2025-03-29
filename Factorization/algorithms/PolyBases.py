from ..math_func import IntegerRoot as introot
from ..math_func import base_rep as bases
from ..algorithms import QuadraticBases as qb
from sympy import symbols, poly, factor_list

def PolyBases(n):
    """
    Input: an integer n>0.
    Output: A boolean integer pair. Returns (True, d) for a proper divisor d,
    otherwise returns (False, n).
    """

    r=introot.IntegerRootGem(n,3)
    t = symbols('t')

    for i in range(2,r+1):
        base_i=bases.base_rep(n,i)
        f=poly(sum(base_i[j]*t**j for j in range(len(base_i))), t)
        boo=f.is_irreducible
        if not boo:
            factors=factor_list(f)
            if factors[0] !=1:
                return (True, factors[0])
            else:
                return (True, factors[1][0][0].eval(i))
            
    return qb.QuadraticBases(n)

