def is_square(n):
    """
    Input: a positive integer n.
    Output: a boolean integer pair. Returns (True, x) if x**2=n. Returns (False, n) otherwise
    """
    m=n
    ## Reduction by powers of 4 with bit-logic
    while n&3 == 0:    
        n=n>>2

    ## Simple bit-logic test. All perfect squares, in binary,
    ## end in 001, when powers of 4 are factored out.
    if n&7 != 1:
        return (False, n)

    if n==1:
        pow=len(bin(m))-2
        half=pow//2
        return (True, 2**half)  ## is power of 4, or even power of 2


    ## Simple modulo equivalency test
    c = n%10
    if c in {3, 7}:
        return (False, m)  ## Not 1,4,5,6,9 in mod 10
    if n % 7 in {3, 5, 6}:
        return (False, m)  ## Not 1,2,4 mod 7
    if n % 9 in {2,3,5,6,8}:
        return (False, m)  
    if n % 13 in {2,5,6,7,8,11}:
        return (False, m)  

    ## Other patterns
    if c == 5:  ## if it ends in a 5
        if (n//10)%10 != 2:
            return (False, m)    ## then it must end in 25
        if (n//100)%10 not in {0,2,6}: 
            return (False, m)    ## and in 025, 225, or 625
        if (n//100)%10 == 6:
            if (n//1000)%10 not in {0,5}:
                return (False, m)    ## that is, 0625 or 5625
    else:
        if (n//10)%4 != 0:
            return (False, m)    ## (4k)*10 + (1,9)


    ## Babylonian Algorithm. Finding the integer square root.
    ## Root extraction.
    s = (len(str(n))-1) // 2
    x = (10**s) * 4

    diff=len(bin(m))-len(bin(n))
    A = {x, n}
    while x * x != n:
        x = (x + (n // x)) >> 1
        if x in A:
            return (False, m)
        A.add(x)
    
    half=diff//2
    d=x*(2**half)
    return (True, d)

