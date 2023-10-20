p = 26513
q = 32321

def iHateEuclid(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (g, u, v) = iHateEuclid(q % p, p)
        return (g, v - (q // p) * u, u)
    
g, u, v = iHateEuclid(p,q)

print("gcd: ", g, " u: ", u, " v: ", v)