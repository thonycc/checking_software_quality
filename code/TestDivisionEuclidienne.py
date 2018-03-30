import unittest

def div_eucl(a,b):
    q = a//b    # Division entière
    r = a%b     # Opérateur 'modulo' qui renvoie le reste
    return (q,r)

class TestStringMethods(unittest.TestCase):

    def testDiv(self):
        self.assertEqual(div_eucl(5,2),(2,1))

unittest.main()
