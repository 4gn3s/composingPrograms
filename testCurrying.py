import unittest

class TestCurrying(unittest.TestCase):
    def testAdd():

        @currying
        def add(x, y):
            return x + y

        assertEqual(add(7,8), 15)
        add3 = add(3)
        assertEqual(add3(7), 10)
        assertEqual(add3(3), 6)
