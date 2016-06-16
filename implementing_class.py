def bind_method(value, instance):
    if callable(value):
        def method(*args):
            return value(instance, args)
        return method
    else:
        return value

def make_instance(cls):
    """
    return a new object instance (is a dispatch dict)
    """
    def get_value(name):
        if name in attributes:
            return attributes[name]
        else:
            # if name is missing from the local storage,
            # look it up in the class
            value = cls['get'](name)
            return bind_method(value, instance)
    
    def set_value(name, value):
        attributes[name] = value
        
    attributes = {}
    instance = {
        'get': get_value,
        'set': set_value
    }
    return instance

def init_instance(cls, *args):
    instance = make_instance(cls)
    init = cls['get']('__init__')
    if init:
        init(instance, *args)
    return instance

def make_class(attributes, base_class=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    
    def set_value(name, value):
        attributes[name] = value
        
    def new(*args):
        return init_instance(cls, *args)
    
    cls = {
        'get': get_value,
        'set': set_value,
        'new': new
    }
    return cls
    
def make_account_class():
    interest = 0.02
    def __init__(self, account_holder):
        self['set']('holder', account_holder)
        self['set']('balance', 0)
    def deposit(self, amount):
        new_balance = self['get']('balance') + amount[0]
        self['set']('balance', new_balance)
        return self['get']('balance')
    def withdraw(self, amount):
        balance = self['get']('balance')
        if amount[0] > balance:
            return "Insufficient funds"
        new_balance = balance - amount[0]
        self['set']('balance', new_balance)
        return self['get']('balance')
    return make_class(locals())

Account = make_account_class()

k = Account['new']('Kirk')
print("interest: ", k['get']('interest'))
print("balance: ", k['get']('balance'))
print("depositing 20: ", k['get']('deposit')(20))
print("withdrawing 5: ", k['get']('withdraw')(5))
k['set']('interest', 0.04)
print("changed interest: ", k['get']('interest'))
print("Account interest: ", Account['get']('interest'))

def make_checking_account_class():
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, (amount[0] + fee,))
    return make_class(locals(), Account)
    
CheckingAccount = make_checking_account_class()

s = CheckingAccount['new']('Spock')
print("interest: ", s['get']('interest'))
print("balance: ", s['get']('balance'))
print("depositing 20: ", s['get']('deposit')(20))
print("withdrawing 5 (plus fee): ", s['get']('withdraw')(5))
s['set']('interest', 0.05)
print("changed interest: ", s['get']('interest'))
print("CheckingAccount interest: ", CheckingAccount['get']('interest'))
