class Account:
    # class attributes are shared accross all objects of a given class
    interest = 0.02
    
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

a = Account('Kirk')
assert a.balance == 0
assert a.holder == 'Kirk'
assert a.deposit(100) == 100
assert a.withdraw(25) == 75
assert a.balance == 75
assert getattr(a, 'balance') == 75
assert hasattr(a, 'deposit')

# calling methods two ways
Account.deposit(a, 1000)
a.deposit(1000)

assert a.balance == 2075
s = Account('Spock')
assert not a.balance == s.balance
assert a.interest == s.interest

prev_class_attr_value = a.interest

# single assignment changes the value for all instances
Account.interest = 0.04
assert prev_class_attr_value != a.interest

# however, if we assign new value to the attribute of an account instance, it changes just one value
s.interest = 0.08
assert a.interest != s.interest

# and class attribute change won't affect it
Account.interest = 0.05
assert s.interest == 0.08

class CheckingAccount(Account):
    """
    an account where withdrawals are charged
    """
    withdraw_charge = 1
    interest = 0.01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

ca = CheckingAccount('Lamus')
assert ca.deposit(10) == 10
assert ca.withdraw(5) == (5 - 1)

# python 3 supports multiple inheritance!
class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)
        
class CrazyStudentAccount(CheckingAccount, SavingsAccount):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1 # a free $$$
        
student = CrazyStudentAccount('John Smith')
assert student.balance == 1
assert student.deposit(100) == 99
assert student.withdraw(10) == 88

Account.__bool__ = lambda self: self.balance != 0

if not ca:
    print("Lamus has nothing") # not gonna be printed, ca.balance != 0
if not Account('empty'):
    print('empty account') # by default the balance is 0, so will be printed
