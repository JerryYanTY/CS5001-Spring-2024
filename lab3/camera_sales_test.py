import unittest
from unittest import mock
from camera_sales import *

class TestCameraSales(unittest.TestCase):

	@mock.patch('camera_sales.input', create=True)
	def test_get_cameras_sold(self, mocked_input):
		expected_result = 5
		mocked_input.side_effect = [expected_result]		
		self.assertEqual(get_cameras_sold(), expected_result)

	@mock.patch('camera_sales.input', create=True)
	def test_get_camera_price(self, mocked_input):
		expected_result = 245.99
		mocked_input.side_effect = [expected_result]		
		self.assertAlmostEqual(get_camera_price(), expected_result)

	def test_calculate_total_pay_1(self):
		self.assertAlmostEqual(calculate_total_pay(5, 20450), 4545)

	def test_calculate_total_pay_2(self):
		self.assertAlmostEqual(calculate_total_pay(75, 255.99), 16883.985)

if __name__ == '__main__':
    unittest.main()