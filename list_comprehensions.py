def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]
    
def keep_if(filter_fn, s):
    return [x for x in s if filter_fn(x)]
    
def reduce(reduce_fn, s, initial_value):
    reduced = initial_value
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced
    
assert reduce(lambda x, y: x*y, [2,4,8], 1) == 64

def divisors_of(n):
    divides = lambda x: n % x == 0
    return [1] + keep_if(divides, range(2, n))
    
assert len(divisors_of(12)) == 5

def sum_of_divisors(n):
    return reduce(lambda x,y: x+y, divisors_of(n), 0)

def is_perfect_number(n):
    return sum_of_divisors(n) == n
    
print("perfect numbers < 1000:")
print(keep_if(is_perfect_number, range(1, 1000)))
