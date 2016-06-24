def sum_digits(n):
    """
    Algorithm based on:
    18117 % 10 = 7
    18117 // 10 = 1811
    """
    if n < 10:
        return n
    prefix, last = n // 10, n % 10
    return sum_digits(prefix) + last
    
def factorial_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total
    
assert factorial_iter(4) == (1*2*3*4)

def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)
    
assert factorial_rec(4) == factorial_iter(4)

# mutual recursion: 2 functions which call each other

def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)
    
def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
    
assert is_even(4)
assert is_odd(5)
assert not is_odd(6)

def fibonacci_rec(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)
    
assert fibonacci_rec(6) == 5

def count_partitions(n, m):
    """
    the number of partitions of n using parts up to m
    (the number of ways in which n can be expressed as sum of positive integers up to m in increasing order)
    
    The number of ways to partition n using integers up to m equals:
    * the number of ways to partition n-m using integers up to m, and
    * the number of ways to partition n using integers up to m-1.
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    return count_partitions(n-m, m) + count_partitions(n, m-1)

assert count_partitions(6, 4) == 9

def count(f):
    """
    allows to count how many times a recursive function has been called
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

fibonacci_rec = count(fibonacci_rec)
print("Fibonacci's 20th number: ", fibonacci_rec(20))
print("Number of calls to fib() used: ", fibonacci_rec.call_count)

# memoization can be used as a higher order function
# it creates a cache of previously computed results indexed by the arguments
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

counted_fib = count(fibonacci_rec)
fibonacci_rec = memo(counted_fib)
print("Fibonacci's 20th number: ", fibonacci_rec(20))
print("Number of calls to fib() used: ", counted_fib.call_count)
