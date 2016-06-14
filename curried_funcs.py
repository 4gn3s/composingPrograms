def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h
    
assert curried_pow(2)(3) == 8

def curry2args(f):
    """
    return a curried version of a 2 argument function
    """
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g
    
def uncurry2args(g):
    """
    return a 2-argument version of a curried function
    """
    def f(x, y):
        return g(x)(y)
    return f
    
curried_pow_prim = curry2args(pow)
assert curried_pow_prim(2)(3) == 8

assert uncurry2args(curried_pow_prim)(2, 3) == 8
