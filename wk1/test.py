import new
import unittest
from solution import calculator

class TestSolution(unittest.TestCase):
  def test_addition(self):
    self.assertTrue(calculator(10,20, "+"),30)
  def test_subtraction(self):
    self.assertTrue(calculator(20,10, "-"),10)
  def test_assert_input_is_not_string(self):
  	self.assertRaises(TypeError,(calculator('a','b','-')))
  def test_multiplication(self):
  	self.asserttrue(calculator(20,10,"*"))