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

def make_adder(n):
    def adder(k):
        return n + k
    return adder
    
add_three = make_adder(3)
assert add_three(4) == 7

class Adder:
    def __init__(self, n):
        self.n = n 
    def __call__(self, k):
        return self.n + k
        
add_three_obj = Adder(3)
assert add_three_obj(4) == 7
