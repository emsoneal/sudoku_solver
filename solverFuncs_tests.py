#Project 3

#Name: Emily O'Neal
#Instructor: Mike Ryu
#Section: 13
import unittest
from solverFuncs import *

class TestCases(unittest.TestCase):
	def test_check_rows_valid_1(self):
		self.assertTrue(check_rows_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ]))

	def test_check_rows_valid_2(self):
		self.assertFalse(check_rows_valid([[1,2,3,4,5], [3, 3, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ]))

	def test_check_rows_valid_3(self):
		self.assertFalse(check_rows_valid([[1,2,3,1,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ]))

	def test_check_rows_valid_4(self):
		self.assertFalse(check_rows_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,2] ]))
	def test_check_rows_valid_5(self):
		self.assertTrue(check_rows_valid([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ]))

	def test_check_rows_valid_6(self):
		self.assertTrue(check_rows_valid([[1,2,3,4,5], [2,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ]))


	def test_check_columns_valid_1(self):
		self.assertFalse(check_columns_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,2] ]))

	def test_check_columns_valid_2(self):
		self.assertTrue(check_columns_valid([[1,1,1,1,1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5,5,5,5,5] ]))

	def test_check_columns_valid_3(self):
		self.assertFalse(check_columns_valid([[1,1,1,1,1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5,5,5,4,5] ]))

	def test_check_columns_valid_4(self):
		self.assertTrue(check_columns_valid([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ]))

	
	def test_check_cages_valid_1(self):
		self.assertTrue(check_cages_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[ [5,2,1,2] ]))

	def test_check_cages_valid_2(self):
		self.assertTrue(check_cages_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[[8,3,5,10,16] ]))

	def test_check_cages_valid_3(self):
		self.assertFalse(check_cages_valid( [ [1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[ [8,2,5,10] ] ) )

	def test_check_cages_valid_4(self):
		self.assertFalse(check_cages_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[[8,3,12,14,16] ]))
	
	def test_check_cages_valid_5(self):
		self.assertTrue(check_cages_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[ [5,2,1,2], [6,2,5,12] ]))

	def test_check_cages_valid_6(self):
		self.assertTrue(check_cages_valid([[1,2,0,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[ [5,2,1,2], [6,2,5,12] ]))

	def test_check_cages_valid_7(self):
		self.assertFalse(check_cages_valid([[1,2,0,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[ [5,2,1,2], [7,2,5,12] ]))
	#def test_check_cages_valid_8(self):
		#self.assertFalse(check_cages_valid([[1,2,0,4,5], [0, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 3, 3, 2, 1], [1,2,3,4,5] ] ,[ [5,2,1,2], [9,2,5,12] ]))


	
	def test_check_valid_1(self):
		self.assertFalse(check_valid([[1,2,3,4,5], [3, 4, 2, 5, 1], [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1,2,3,4,5] ] ,[ [5,2,1,2] ]))

	def test_check_valid_2(self):
		self.assertTrue(check_valid([[1,2,3,5,4], [5,3,4,2,1], [4,5,2,1,3], [3,1,5,4,2], [2,4,1,3,5] ] ,[ [5,2,4,9], [8,3,11,12,13] ]))

	def test_check_cages_valid_9(self):
		self.assertTrue(check_cages_valid([[1,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ], [[9, 3, 0, 5, 6,], [7, 2, 1, 2], [10, 3, 3, 8, 13], [14, 4, 4, 9, 14, 19], [3, 1, 7], [8, 3, 10, 11, 16], [13, 4, 12, 17, 21, 22], [5, 2, 15, 20], [6, 3, 18, 23, 24]]))
if __name__ == '__main__':
   unittest.main()
