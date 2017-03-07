import unittest

from prime_numbers import get_primes

class TestPrimeNumbers(unittest.TestCase):
	def test_returns_correct_primes(self):
		self.assertTrue(get_primes(20),[1,3,5,7,11,13,17,19])
	def test_assert_input_is_not_string(self):
		self.assertRaises(TypeError,get_primes('a_string'))
	def test_asserts_input_not_negative(self):
		self.assertIs(get_primes(-10),'Please don\'t input negatives')
	def test_returns_primes_in_array(self):
		# Result should be an array
		self.assertIsInstance(get_primes(20), List)
	def test_assert_input_not_even_num(self):
		# result shouldnt print even numbers
		self.assertRaises(TypeError,get_primes('even_num'))
