'''
 Test cases example for lab 01.

 Name: Joanna Chou
 Section: 07/08
'''

import unittest      # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# Much of this code should be viewed as boilerplate for now.
#
class TestsLab1(unittest.TestCase):
   def test_expressions(self):         # Defines one testing function.
      self.assertEqual(2 + 3, 5)
      # Add code after this line (like the line above) for the additional test cases.
   def test_expressions2(self): 
        self.assertEqual(2 * 3, 6)
   def test_expressions3(self): 
        self.assertEqual(2 ** 3, 8)
   def test_expressions4(self):
        self.assertEqual(49 // 3, 16)
   def test_expressions5(self):
        self.assertAlmostEqual(49 / 3, 16.333333333333332)
   def test_expressions6(self):
        self.assertEqual(49 % 3, 1)
   def test_expressions7(self):
        self.assertEqual(7 * 2 + 29 // 3 - 2 , 21)
   def test_expressions8(self):
        self.assertEqual(7 * (2 + 29) // 3 - 2, 70)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
