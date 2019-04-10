import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr_1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_repr_2(self):                                                      
        loc = Location("Bakersfield", 35.3, 119.7)                                     
        self.assertEqual(repr(loc),"Location('Bakersfield', 35.3, 119.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc == loc2, True)

    def test_eq_2(self):                                                          
        loc = Location("Bakersfield", 35.3, 119.7)                                     
        loc2 = Location("SLO", 35.3, -120.7)                                    
        self.assertEqual(loc == loc2, False)

if __name__ == "__main__":
        unittest.main()
