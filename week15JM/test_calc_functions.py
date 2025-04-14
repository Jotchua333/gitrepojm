import unittest
import calc_functions

#Inheriting testCase class from unittest module
class Tests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc_functions.add(10, 5), 15)
    def test_sub(self):
        self.assertEqual(calc_functions.sub(10, 5), 5)

if __name__ == '__main__':
    unittest.main()