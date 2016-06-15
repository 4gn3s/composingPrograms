def pair(x, y):
    def get(index):
        if index == 0:
            return x
        else:
            return y
    return get
    
def select(pair, index):
    return pair(index)
    
p = pair(2, 19)
assert select(p, 0) == 2
assert select(p, 1) == 19
