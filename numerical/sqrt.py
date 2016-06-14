from common import approx_eq, improve

def average(x, y):
    return (x + y) / 2

def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_stop(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_stop)
