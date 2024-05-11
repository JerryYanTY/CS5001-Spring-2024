import unittest
from find_greater import find_greater


class TestFindGreater(unittest.TestCase):
    def test_no_greater(self):
        self.assertEqual(find_greater([1,2,3,4,5],0), 5)

    def test_one_greater(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5], 1), 4)

    def test_two_greater(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5], 2), 3)

    def test_great_than_three(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5], 3), 2)

    def test_greater_than_four(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5], 4), 1)

    def test_greater_than_five(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5], 5), 0)
    def larger_list_n_3(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5, 6, 7, 8, 9], 6), 3)

    def larger_list_n_2(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5, 6, 7, 8, 9], 7), 2)

    def larger_list_n_1(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 1)

    def larger_list_n_0(self):
        self.assertEqual(find_greater([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 0)


if __name__ == '__main__':
    unittest.main()
