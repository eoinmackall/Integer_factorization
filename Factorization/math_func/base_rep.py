def base_rep(n,z):
    """
    Input: integers n>z>0
    Output: A list [b_0,b_1,b_2,..] so that n=(...b_2b_1b_0)_z.
    """

    f=[]
    i=0
    while n>0:
        (n,c)=divmod(n,z)
        f.append(c)
        i+=1
    return f