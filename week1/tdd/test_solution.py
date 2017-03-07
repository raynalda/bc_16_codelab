test_solution.py


import unittest
from tdd import solution

class test_solution(unittest.testcase):
	def addition(self):
		self.assertTrue(solution(10,20,"+"))

if __name__ == "__main__":
    unittest.main()
     		

		
