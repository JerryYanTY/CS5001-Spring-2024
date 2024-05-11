import unittest
from unittest import mock
from count_ing_words import count_ing_words

class TestCountIngWords(unittest.TestCase):
    @mock.patch('count_ing_words.input', create=True)
    def test_count_ing_words_base(self, mocked_input):
        expected_result = 2
        mocked_input.side_effect = ['orange', 'counting', 'apple', 'grading', 'quit']
        self.assertEqual(count_ing_words(), expected_result)

    @mock.patch('count_ing_words.input', create=True)
    def test_count_ing_words_zero_result(self, mocked_input):
        expected_result = 0
        mocked_input.side_effect = ['orange', 'banana', 'apple', 'pear', 'quit']
        self.assertEqual(count_ing_words(), expected_result)


    @mock.patch('count_ing_words.input', create=True)
    def test_count_ing_words_all(self, mocked_input):
        expected_result = 4
        mocked_input.side_effect = ['hearing', 'seeing', 'feeling', 'knowing', 'quit']
        self.assertEqual(count_ing_words(), expected_result)


    @mock.patch('count_ing_words.input', create=True)
    def test_count_ing_words_no_input(self, mocked_input):
        expected_result = 0
        mocked_input.side_effect = ['quit']
        self.assertEqual(count_ing_words(), expected_result)


    @mock.patch('count_ing_words.input', create=True)
    def test_count_ing_words_long_input(self, mocked_input):
        expected_result = 6
        mocked_input.side_effect = ['one', 'two', 'playing','coding', 'three', 'four', 'staying', 'working', 'eating', 'five', 'looping', 'quit']
        self.assertEqual(count_ing_words(), expected_result)


    @mock.patch('count_ing_words.input', create=True)
    def test_count_ing_words_example_output(self, mocked_input):
        expected_result = 3
        mocked_input.side_effect = ['waiting', 'enjoy', 'happy','working', 'flying', 'quit']
        self.assertEqual(count_ing_words(), expected_result)


if __name__ == '__main__':
    unittest.main()
