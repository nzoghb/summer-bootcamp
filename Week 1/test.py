# B@B Summer Bootcamp
# Assignment 1
# See Notebook 1 for help

import unittest
from Assignment1 import *


class test1(unittest.TestCase):
    def test_int_to_word(self):
        self.assertEqual(int_to_word(1), "One")
        self.assertEqual(int_to_word(2), "Two")
        self.assertEqual(int_to_word(3), "Three")
        self.assertEqual(int_to_word(4), "Four")
        self.assertEqual(int_to_word(5), "Five")
        self.assertEqual(int_to_word(10),
            "Sorry, I don't recognize that number")
        self.assertEqual(int_to_word("hello"),
            "Sorry, I don't recognize that number")

    def test_two_of_three(self):
        self.assertEqual(two_of_three(1, 2, 3), 13)
        self.assertEqual(two_of_three(5, 3, 1), 34)
        self.assertEqual(two_of_three(10, 2, 8), 164)
        self.assertEqual(two_of_three(5, 5, 5), 50)

    def test_decades_ago(self):
        self.assertEqual(decades_ago(1995), 2.2)
        self.assertEqual(decades_ago(2017), 0)
        self.assertEqual(decades_ago(2015), 0.2)
        self.assertEqual(decades_ago(2007), 1.0)

    def test_if_function(self):
        self.assertEqual(if_function(True, 2, 3), 2)
        self.assertEqual(if_function(False, 2, 3), 3)
        self.assertEqual(if_function(3==2, 3+2, 3-2), 1)
        self.assertEqual(if_function(3>2, 3+2, 3-2), 5)

    def test_sum_of_largest_smallest(self):
        self.assertEqual(sum_of_largest_smallest([1, 2, 3, 4, 5]), 6)
        self.assertEqual(sum_of_largest_smallest([7]), 14)
        self.assertEqual(sum_of_largest_smallest([]), 0)

if __name__ == '__main__':
    unittest.main()
