def account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Insufficient funds"
        balance -= amount
        return balance
    dispatch = {
        'deposit': deposit,
        'withdraw': withdraw
    }
    return dispatch
    
a = account(100)
print(a['withdraw'](25))  # 75
print(a['withdraw'](25))  # 50
print(a['withdraw'](60))  # Insufficient funds
print(a['withdraw'](40))  # 10
print(a['deposit'](100))  # 110

from linked_lists import empty, len_list, getitem_list, link, first, rest, join

def mutable_list():
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_list(contents)
        elif message == 'getitem':
            return getitem_list(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join(contents, ", ")
    return dispatch

def to_mutable_list(s):
    new_s = mutable_list()
    for elem in reversed(s):
        new_s('push_first', elem)
    return new_s
    
s = to_mutable_list(['bob', 'charlie', 'alice'])
print(s('str'))
s('push_first', 'dave')
print(s('str'))
print(s('len'))
print(s('getitem', 3))
print(s('pop_first'))
print(s('str'))


def dictionary():
    records = []
    
    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value
    
    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = [[key, value]] + non_matches
        
    def length():
        return len(records)
        
    def dispatch(message, key=None, value=None):
        if message == 'get':
            return getitem(key)
        elif message == 'set':
            setitem(key, value)
        elif message == 'len':
            return length()
    
    return dispatch
    
d = dictionary()
d('set', 1, 'lettuce')
d('set', 2, 'tomato')
print(d('get', 1))
print(d('len'))
