# Python's built in testing framework is unittest. 
# It is often used as a base for other testing frameworks.
# though some test runners make things simpler, unittest has a lot of features
# that remain useful, popular, and many test frameworks are built on top of it.
import unittest 
# Note: we'll look at the very popular pytest later. 

# We need to import the things we are testing.
from functions import is_anagram, duplicates
from classes import Averages


# The unittest framework requires us to format tests in a specific way.
# We need to create a class that inherits from unittest.TestCase.
# each method of the class that starts with "test" will be run as a test.
# "helper" methods can be created to facilitate testing, but they should not
# start with "test" or they will be run as tests.

# How you organize your tests is up to you, but generally you want to group
# related tests together in a class. We'll make one class per "thing" being tested
# where the "things" are the two functions from functions.py and the class from classes.py
# So we'll have three classes in this file.


class TestIsAnagram(unittest.TestCase):
    # NOTE: Docstrings are printed during test runs at higher levels of
    # verbosity, so they can be useful.

    def test_identifies_anagrams(self):
        '''Test that is_anagram correctly identifies actual anagrams'''
        # the TestCase class exposes many useful "assert" functions that are
        # used to check the output of your functions.
        self.assertTrue(is_anagram('abba', 'aabb'))
        self.assertTrue(is_anagram('the detectives', 'detect thieves'))
        self.assertTrue(is_anagram('abcde', 'ebcda'))
        self.assertTrue(is_anagram('aaaa', 'aaaa'))

    def test_identifies_non_anagrams(self):
        self.assertFalse(is_anagram('aab', 'bba'))
        self.assertFalse(is_anagram('abcde', 'abcdf'))
        self.assertFalse(is_anagram('bab', 'aba'))
        self.assertFalse(is_anagram('aaaa', 'aaa'))

    def test_case_sensitive(self):
        self.assertFalse(is_anagram('AbA', 'aba'))
        self.assertTrue(is_anagram('abA', 'Aba'))
        # Micro-exercise: Add one more test to check that case sensitivity is 
        # working correctly.

###################################################################################
# INSTRUCTOR NOTE: Show the last 2 lines of code and run the tests before moving on
###################################################################################

class TestDuplicates(unittest.TestCase):
    def test_finds_duplicates(self):
        self.assertEqual(duplicates([1, 2, 3, 1]), [1])
        self.assertEqual(duplicates([3, 3, 3, 3, 3]), [3])
        self.assertEqual(duplicates([1, 2, 3, 4, 1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(duplicates([1, 1, 2, 3, 3, 4]), [1, 3])

    def test_no_duplicates(self):
        self.assertEqual(duplicates([1, 2, 3, 4, 5, 6]), [])
        self.assertEqual(duplicates([1, 2, 3]), [])
        self.assertEqual(duplicates([]), [])
    

class TestAverages(unittest.TestCase):
    def test_mean(self):
        a = Averages([1, 2, 3, 4, 5])
        self.assertEqual(a.mean(), 3)
        a = Averages([1, 1, 1, 1, 1])
        self.assertEqual(a.mean(), 1)
        a = Averages([1, 2, 3, 4, 5, 6])
        self.assertEqual(a.mean(), 3.5)

    def test_median(self):
        a = Averages([1, 2, 3, 4, 5])
        self.assertEqual(a.median(), 3)
        a = Averages([1, 1, 1, 1, 1])
        self.assertEqual(a.median(), 1)
        a = Averages([1, 2, 3, 4, 5, 6])
        self.assertEqual(a.median(), 3.5)
        a = Averages([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(a.median(), 4)
        a = Averages([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(a.median(), 4.5)

    def test_makes_a_copy(self):
        # Micro-exercise: finish this function so that it tests whether or
        # not the data attribute is a copy of the input data. You should test
        # that the lists are equal, but not the same list in memory.
        pass


# A common way to run tests is to use a test runner.
# These two lines of code make it so that when we run this 
# speficic file, the tests will run using unittest's built in test runner.
if __name__ == "__main__":
    unittest.main()
    # unittest.main(verbosity=2) # This will give more detailed output

### ADDITIONALLY ###
# You can run these tests from the command line by running the following from 
# the folder containing tests.py:
'python -m unittest tests.py'

# Micro-exercise: Introduce an failure by intentionally breaking one of the
# tests above, then run the code to see what a failure looks like.