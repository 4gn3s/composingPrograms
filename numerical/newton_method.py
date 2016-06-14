from __future__ import division
from common import approx_eq, improve
    
def newton_update(f, df):
    def update(x):
        return x - f(x) / df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def sqrt_newton(a):
    """
    Allows to find a square root of a number using Newton's method applied to
    a function x*x - a, which has a zero in sqrt(a)
    """
    def f(x):
        return x * x - a
    def df(x):
        return 2 * x
    return find_zero(f, df)

def power(x, n):
    """
    returns x * x * ... * x repeated n times
    """
    product, k = 1, 0
    while k < n:
        product, k = product * x, k + 1
    return product
    
def nth_root(n, a):
    """
    Generalization of sqrt_newton where n = 2. To calculate a root of degree n,
    we use a function x^n - a
    """
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)

assert sqrt_newton(64) == 8.0
assert nth_root(2, 64) == sqrt_newton(64)
assert nth_root(3, 64) == 4.0
