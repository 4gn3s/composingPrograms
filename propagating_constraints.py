from operator import add, sub, mul, truediv
# building a constraint-based system (type of declarative programming)
#
# a sketch of a general model of linear relationships
# e.g. adder(a,b,c) enforces that a + b = c
# such constraints will be combined: joined by connectors (A connector has a single value)
# e.g. Celsius/Fahrenheit:
# 9 * c = 5 * (f - 32)
# w = 9, x = 5, y = 32
# u = 9 * c, v = (f - 32)
#
# constraints: dictionaries, do not hold local states themselves
# a message passing system to coordinate constraints and connectors
# constraints' responses to messages are non-pure functions that change the connectors that they constrain
# connectors: dictionaries that hold a current value and respond to messages that manipulate that value

# types of messages for connectors:
# connector['set_val'](source, value) indicates that the source is requesting the connector to set its current value to value.
# connector['has_val']() returns whether the connector already has a value.
# connector['val'] is the current value of the connector.
# connector['forget'](source) tells the connector that the source is requesting it to forget its value.
# connector['connect'](source) tells the connector to participate in a new constraint, the source.
#
# types of messages for constraints:
# constraint['new_val']() indicates that some connector that is connected to the constraint has a new value.
# constraint['forget']() indicates that some connector that is connected to the constraint has forgotten its value.

def inform_all_except(source, message, constraints):
    for c in constraints:
        if c != source:
            c[message]()

def connector(name=None):
    
    informant = None # The source of the current val
    constraints = [] # A list of connected constraints
    
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, "=", value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('contradition detected: ', val, ' vs ', value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, ' is forgotten.')
            inform_all_except(source, 'forget', constraints)

    connector = {
        'val': None,
        'set_val': set_value,
        'forget': forget_value,
        'has_val': lambda: connector['val'] is not None,
        'connect': lambda source: constraints.append(source)
    }
    return connector

def make_trenary_constaint(a, b, c, ab, ca, cb):
    def new_value():
        """
        new_value is called whenever the constraint is informed that one of its connectors has a value
        This function first checks to see if both a and b have values. 
        If so, it tells c to set its value to the return value of function ab, which is add in the case of an adder
        The constraint passes itself (constraint) as the source argument of the connector, which is the adder object
        """
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        """
        If the constraint is informed that one of its connectors has forgotten its value, 
        it requests that all of its connectors now forget their values
        """
        for connector in (a, b, c):
            connector['forget'](constraint)

    constraint = {'new_val': new_value, 'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

def adder(a, b, c):
    """
    the constraint that a + b = c implies that c - a = b and c - b = a
    """
    return make_trenary_constaint(a, b, c, add, sub, sub)
    
def multiplier(a, b, c):
    return make_trenary_constaint(a, b, c, mul, truediv, truediv)
    
def constant(connector, value):
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def converter(c, f):
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')

converter(celsius, fahrenheit)

# the user sets the value of celsius
celsius['set_val']('user', 25)

# the user sets the value of fahrenheit
# this should not work: the value is already set (by constraint)
fahrenheit['set_val']('user', 212)

# to fix it, we can ask celsius to forget it's value
celsius['forget']('user')

assert celsius['has_val']() == False
assert fahrenheit['has_val']() == False

# now this works, and forces the celsius to have new value
fahrenheit['set_val']('user', 212)
