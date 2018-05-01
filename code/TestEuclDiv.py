import unittest
from EuclDiv import div_eucl

# First test sequence
class TestStringMethods1(unittest.TestCase):

    def testDiv(self):
        self.assertEqual(div_eucl(5,2),(2,1))

    def testDiv1(self):
        self.assertEqual(div_eucl(7,2),(3,1))

    def testDiv2(self):
        self.assertEqual(div_eucl(9,3),(3,0))

# Second test sequence
class TestStringMethods2(unittest.TestCase):

    def testDiv3(self):
        self.assertEqual(div_eucl(15,2),(7,1))

    def testDiv4(self):
        self.assertEqual(div_eucl(8,1),(7,0))# Expected failure

#Test suite composed of the 2 previous test sequences
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestStringMethods1))
suite.addTest(unittest.makeSuite(TestStringMethods2))

unittest.main()
