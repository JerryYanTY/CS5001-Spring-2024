import unittest
from passwordify import passwordify


class TestPasswordify(unittest.TestCase):
    def test_base(self):
        self.assertEqual(passwordify("AeopFabe"), "AeopFabe")

    def test_space(self):
        self.assertEqual(passwordify("Aeop Fabe"), "Aeop-Fabe")

    def test_s(self):
        self.assertEqual(passwordify("AesopsFabes"), "Ae$op$Fabe$")

    def test_l(self):
        self.assertEqual(passwordify("AesopsFables"), "Ae$op$Fab1e$")

    def test_multiple(self):
        self.assertEqual(passwordify("Aesops Fables"), "Ae$op$-Fab1e$")

    def test_zero(self):
        self.assertEqual(passwordify("zero"), "0")

    def test_one(self):
        self.assertEqual(passwordify("one"), "1")

    def test_two(self):
        self.assertEqual(passwordify("two"), "2")

    def test_three(self):
        self.assertEqual(passwordify("three"), "3")

    def test_four(self):
        self.assertEqual(passwordify("four"), "4")

    def test_five(self):
        self.assertEqual(passwordify("five"), "5")

    # six and seven not tested as s to $ and l to 1 takes precedence over replacing substrings six and seven

    def test_eight(self):
        self.assertEqual(passwordify("eight"), "8")

    def test_nine(self):
        self.assertEqual(passwordify("nine"), "9")

    def test_ten(self):
        self.assertEqual(passwordify("ten"), "10")


if __name__ == '__main__':
    unittest.main()
