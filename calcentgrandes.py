def multEG(u,v):
    n = max(len(str(u)), len(str(v)))
    if n == 1:
        return u*v
    else:
        s = n // 2
        w = u // (10**s)
        x = u % (10**s)
        y = v // (10**s)
        z = v % (10**s)
        return multEG(w,y)*(10**(2*s)) + (multEG(w,z)+multEG(x,y))*(10**s) + multEG(x,z)


print(multEG(5426859751245874,6974845269857426))