class LinkedList:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is LinkedList.empty or isinstance(rest, LinkedList)
        self.first = first
        self.rest = rest
        
    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    
    def __len__(self):
        return len(self.rest) + 1

    def __repr__(self):
        if self.rest is LinkedList.empty:
            rest = ''
        else:
            rest = ', ' + self.rest.__repr__()
        return '({0}{1})'.format(self.first, rest)
        
    def is_empty(self):
        return self is LinkedList.empty
        
    def contains(self, value):
        if self.is_empty():
            return False
        elif self.first == value:
            return True
        else:
            return self.rest.contains(value)
        
    def map(self, f):
        if self is LinkedList.empty:
            return self
        elif self.rest is LinkedList.empty:
            return LinkedList(f(self.first))
        else:
            return LinkedList(f(self.first), self.rest.map(f))
            
    def filter(self, f):
        if self is LinkedList.empty:
            return self
        else:
            if self.rest is LinkedList.empty:
                filtered = ()
            else:
                filtered = self.rest.filter(f)
            if f(self.first):
                return LinkedList(self.first, filtered)
            return filtered
            
    def join(self, separator=", "):
        if self is LinkedList.empty:
            return ""
        elif self.rest is LinkedList.empty:
            return str(self.first)
        else:
            return str(self.first) + separator + self.rest.join(separator)
            
    def adjoin(self, value):
        """returns a set of all elements of self including the value"""
        if self.contains(value):
            return self
        else:
            return LinkedList(value, self)
        
def extend(s, t):
    if s is LinkedList.empty:
        return t
    else:
        return LinkedList(s.first, extend(s.rest, t))

s = LinkedList(3, LinkedList(4, LinkedList(5)))
assert len(s) == 3
assert s[1] == 4
assert s.contains(5)
print(s)
LinkedList.__add__ = extend
ss = s + s
print(ss)
ssquare = ss.map(lambda x: x*x)
print(ssquare)
odd = lambda x: x % 2 == 1
odds = ssquare.filter(odd)
print(odds)
print(odds.join())

class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches
        
    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.entry, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.entry))
        
    def is_leaf(self):
        return not self.branches

def fib_tree(n):
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        return Tree(left.entry + right.entry, (left, right))

tree = fib_tree(5)
print("TREES")
print(tree)

def sum_entries(tree):
    return tree.entry + sum([sum_entries(branch) for branch in tree.branches])

print(sum_entries(tree))
