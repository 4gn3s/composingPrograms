empty = 'empty'

lista = [1, [2, [3, [4, 'empty']]]]

def is_linked(s):
    return s == empty or len(s) == 2 and is_linked(s[1])
    
def link(first, rest):
    assert is_linked(rest)
    return [first, rest]
    
def first(s):
    assert is_linked(s)
    assert s != empty
    return s[0]
    
def rest(s):
    assert is_linked(s)
    assert s != empty
    return s[1]

l = link(1, link(2, link(3, link(4, empty))))
assert l == lista
assert first(l) == 1
assert is_linked(rest(l))

def len_list(s):
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def len_list_rec(s):
    if s == empty:
        return 0
    return 1 + len_list_rec(rest(s))

assert len_list(l) == 4
assert len_list(l) == len_list_rec(l)

def getitem_list(s, i):
    """
    returns the element at index i
    """
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)
    
def getitem_list_rec(s, i):
    if i == 0:
        return first(s)
    return getitem_list_rec(rest(s), i - 1)

assert getitem_list(l, 3) == 4
assert getitem_list_rec(l, 3) == 4

def merge_lists(s, t):
    """
    returns a list, where the elements of s are followed by the elements of t
    """
    assert is_linked(s) and is_linked(t)
    if s == empty:
        return t
    return link(first(s), merge_lists(rest(s), t))
    
l2 = merge_lists(l, l)

def apply_to_all(f, s):
    assert is_linked(s)
    if s == empty:
        return s
    return link(f(first(s)), apply_to_all(f, rest(s)))

l2squared = apply_to_all(lambda x: x*x, l2)

def keep_if(f, s):
    assert is_linked(s)
    if s == empty:
        return s
    kept = keep_if(f, rest(s))
    if f(first(s)):
        return link(first(s), kept)
    else:
        return kept

print(keep_if(lambda x: x % 2 == 0, l2squared))

def join(s, separator):
    """
    returns a string of all elements joined by the separator
    """
    assert is_linked(s)
    if s == empty:
        return ""
    elif rest(s) == empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join(rest(s), separator)
        
print(join(l2squared, ", "))

def partitions(n, m):
    if n == 0:
        return link(empty, empty) # empty partition
    elif n < 0 or m == 0:
        return empty
    else:
        using_m = partitions(n - m, m)
        with_m = apply_to_all(lambda s: link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return merge_lists(with_m, without_m)

def print_partitions(n, m):
    lists = partitions(n, m)
    strings = apply_to_all(lambda s: join(s, " + "), lists)
    print(join(strings, "\n"))

print(print_partitions(6, 4))
