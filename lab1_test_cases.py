import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter_one_max(self): 
        self.assertEqual(max_list_iter([1,2,3]),3)
        self.assertEqual(max_list_iter([1,3,2]),3)
        self.assertEqual(max_list_iter([3,1,2]),3)
    
    def test_max_list_iter_multiple_max(self):
        self.assertEqual(max_list_iter([1,3,3]),3)
        self.assertEqual(max_list_iter([3,3,2,1]),3)
        self.assertEqual(max_list_iter([3,1,3]),3)

    def test_max_list_iter_all_same(self): 
        self.assertEqual(max_list_iter([-1,-1,-1,-1]),-1)
    
    def test_max_list_iter_empty(self): #Checks for None when list is empty
        self.assertEqual(max_list_iter([]),None)
    
    def test_max_list_iter_none(self): 
        tlist = None
        with self.assertRaises(ValueError):  #Used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
    
    def test_reverse_rec_none(self): 
        tlist = None
        with self.assertRaises(ValueError): #Used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_all_same(self): 
        self.assertEqual(reverse_rec([3,3,3]),[3,3,3])

    def test_reverse_rec_all_two_same(self): 
        self.assertEqual(reverse_rec([3,2,2]),[2,2,3])
        self.assertEqual(reverse_rec([2,2,3]),[3,2,2])
        self.assertEqual(reverse_rec([2,3,2]),[2,3,2])

    def test_bin_search_1(self):
        list_val = [0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, low, high, list_val), 3)
    
    def test_bin_search_bottom(self):                                                
        list_val = [0,1,2,3,4,7,8,9,10]                                          
        low = 0                                                                 
        high = len(list_val)-1                                                  
        self.assertEqual(bin_search(0, low, high, list_val), 0)

    def test_bin_search_top(self):                                                
        list_val = [0,1,2,3,4,7,8]                                          
        low = 0                                                                 
        high = len(list_val)-1                                                  
        self.assertEqual(bin_search(8, low, high, list_val), 6)

    def test_bin_search_nonzero_low(self):
        list_val = [1,2,3,4,7,8,9]
        low = 2
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), None)
        self.assertEqual(bin_search(7, low, high, list_val), 4)

    def test_bin_search_different_high(self):
        list_val = [1,2,3,4,7,8,9]
        low = 0
        high = 5 
        self.assertEqual(bin_search(9, low, high, list_val), None)
        self.assertEqual(bin_search(8, low, high, list_val), 5)

    def test_bin_search_different_high_and_low(self):
        list_val = [1,2,5,7,8]
        low = 1
        high = 3
        self.assertEqual(bin_search(1, low, high, list_val), None)
        self.assertEqual(bin_search(8, low, high, list_val), None)
        self.assertEqual(bin_search(5, low, high, list_val), 2)

    def test_bin_search_one_item(self):
        list_val = [1]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(1, low, high, list_val), 0)

    def test_bin_search_none(self):
        list_val = None
        low = 0 
        high = 1
        with self.assertRaises(ValueError): #Used to check for exception
            bin_search(4, low, high, list_val)

    def test_bin_search_empty(self): #Checks for None when list is empty
        list_val = []
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, low, high, list_val), None)
 
if __name__ == "__main__":
        unittest.main()

    
