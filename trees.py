def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), "branches have to be trees"
    return [root] + list(branches)
    
def root(tree):
    return tree[0]
    
def branches(tree):
    return tree[1:]
    
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
print(t)
assert root(t) == 3
print branches(t)
assert not is_leaf(t)
assert is_leaf(branches(t)[0])

def fibonacci_tree(n):
    """
    a tree where the n-th fib number is the root
    """
    if n == 0 or n == 1:
        return tree(n)
    left, right = fibonacci_tree(n - 2), fibonacci_tree(n - 1)
    fib_n = root(left) + root(right)
    return tree(fib_n, [left, right])
    
print fibonacci_tree(5)

def count_leaves(tree):
    if is_leaf(tree):
        return 1
    return sum([count_leaves(branch) for branch in branches(tree)])
    
assert count_leaves(fibonacci_tree(5)) == 8

def partition_tree(n, m):
    """
    A partition tree for n using parts up to size m is a binary (two branch) 
    tree that represents the choices taken during computation. In a non-leaf partition tree:
    the left (index 0) branch contains all ways of partitioning n using at least one m,
    the right (index 1) branch contains partitions using parts up to m-1, and
    the root value is m.
    """
    if n == 0:
        return tree(True)
    elif n < 0 or m == 0:
        return tree(False)
    left = partition_tree(n - m, m)
    right = partition_tree(n, m - 1)
    return tree(m, [left, right])

def print_partitions(tree, partition=[]):
    if is_leaf(tree):
        if root(tree):
            print(' + '.join(partition))
    else:
        left, right = branches(tree)
        m = str(root(tree))
        print_partitions(left, partition + [m])
        print_partitions(right, partition)
    
print print_partitions(partition_tree(6, 4))
