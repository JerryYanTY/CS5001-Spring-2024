import unittest
from student import *

class TestStudent(unittest.TestCase):

    def test_init_no_grades(self):
        s = Student('Ally Quinche', 12345)
        self.assertEqual(s.name, 'Ally Quinche')
        self.assertEqual(s.id, 12345)
        self.assertEqual(s.grades, [])

    def test_init_with_grades(self):
        s = Student('Jordan Saberi', 98765, [90, 88])
        self.assertEqual(s.name, 'Jordan Saberi')
        self.assertEqual(s.id, 98765)
        self.assertEqual(s.grades, [90, 88])

    def test_add_grade(self):
        s = Student('Ally Saberi', 99986, [90, 88])
        s.add_grade(89)
        self.assertEqual(sorted(s.grades), sorted([90, 88, 89]))

    def test_get_average(self):
        s = Student('Herby Zhao', 45336, [90, 88])    
        self.assertAlmostEqual(s.get_average(), 89)

    def test_get_average_decimal(self):
        s = Student('Herby Zhao', 45336, [90, 88, 88])    
        self.assertAlmostEqual(s.get_average(), 88.667, 3)

    def test_get_letter_grade_A(self):
        s = Student('Herby Zhao', 45336, [90, 91, 90.5])    
        self.assertAlmostEqual(s.get_letter_grade(), 'A')

    def test_get_letter_grade_B(self):
        s = Student('Herby Zhao', 45336, [82, 82, 89, 83])    
        self.assertAlmostEqual(s.get_letter_grade(), 'B')


    def test_get_letter_grade_C(self):
        s = Student('Herby Zhao', 45336, [90, 60, 74])    
        self.assertAlmostEqual(s.get_letter_grade(), 'C')

    def test_get_letter_grade_F(self):
        s = Student('Herby Zhao', 45336, [90, 0, 44, 80])    
        self.assertAlmostEqual(s.get_letter_grade(), 'F')

if __name__ == '__main__':
    unittest.main()