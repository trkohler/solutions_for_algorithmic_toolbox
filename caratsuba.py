#   // -> divide with integral result (discard remainder)
#   ** -> exponential
#  this algorithm helps multiply very big numbers very fast

def karat(x,y):

    if len(str(x)) < 3 or len(str(y)) < 3:
        return x*y

    n = max(len(str(x)),len(str(y))) // 2

    a = x // 10**(n)
    b = x % 10**(n)
    c = y // 10**(n)
    d = y % 10**(n)

    z0 = karat(b,d)
    z1 = karat((a+b), (c+d))
    z2 = karat(a,c)

    return ((10**(2*n))*z2)+((10**n)*(z1-z2-z0))+z0
