import unittest
from lucky_sum import lucky_sum

class TestLuckySum(unittest.TestCase):

	def test_lucky_sum_1(self):
		self.assertEqual(lucky_sum(1, 2, 3), 6)

	def test_lucky_sum_2(self):
		self.assertEqual(lucky_sum(1, 2, 13), 3)

	def test_lucky_sum_3(self):
		self.assertEqual(lucky_sum(1, 13, 3), 1)

	def test_lucky_sum_4(self):
		self.assertEqual(lucky_sum(1, 13, 13), 1)

	def test_lucky_sum_5(self):
		self.assertEqual(lucky_sum(6, 5, 2), 13)

	def test_lucky_sum_6(self):
		self.assertEqual(lucky_sum(13, 2, 3), 0)

	def test_lucky_sum_7(self):
		self.assertEqual(lucky_sum(13, 13, 2), 0)

	def test_lucky_sum_8(self):
		self.assertEqual(lucky_sum(9, 4, 13), 13)

	def test_lucky_sum_9(self):
		self.assertEqual(lucky_sum(8, 13, 2), 8)

	def test_lucky_sum_10(self):
		self.assertEqual(lucky_sum(7, 2, 1), 10)

	def test_lucky_sum_11(self):
		self.assertEqual(lucky_sum(3, 3, 13), 6)

if __name__ == '__main__':
    unittest.main()