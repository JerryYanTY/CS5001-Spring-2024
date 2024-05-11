from student import Student


class Student_List:
	"""
	Data about a class of students
	"""

	def __init__(self, course, students=None):
		"""Constructor
		Parameters:
		  - course: string description of course (e.g., CS 5001)
		  - students: optional dictionary of id -> Student mapping		
		"""
		self.course = course
		self.students = {}

	def add_student(self, student):
		"""Add a new student to the class.
		Parameters:
		  - student: Student object containing student information		
		Raises an exception if student.id already exists in the 
		class.
		"""
		if student.id in self.students:
			raise Exception("Student's id already exists.")
		else:
			self.students[student.id] = student

	def update_student(self, student_id, new_grade):
		"""Updates a student's grade list with a new score.
		Parameters:
		  - student_id: int representing the id of the student
		  - new_grade: float representing the new score
		Raises an exception if student.id does not exist in the 
		class.
		"""
		if student_id not in self.students:
			raise Exception("Student ID does not exist.")
		else:
			self.students[student_id].add_grade(new_grade)

	def get_student_average(self, student_id):
		"""Returns a student's average grade.
		Parameters:
		  - student_id: int representing the id of the student
		Raises an exception if student.id does not exist in the 
		class.
		"""
		if student_id not in self.students:
			raise Exception("Student ID does not exist.")
		else:
			return self.students[student_id].get_average()

	def get_student_letter_grade(self, student_id):
		"""Retrusn a student's letter grade.
		Parameters:
		  - student_id: int representing the id of the student
		Raises an exception if student.id does not exist in the 
		class.
		"""
		if student_id not in self.students:
			raise Exception("Student ID does not exist.")
		else:
			return self.students[student_id].get_letter_grade()

	def __str__(self):
		"""Returns a string representation of the class.
		Note: in oder for this to work correctly you must have
		an instance variable named course that is a string and 
		an instance variable named students that is a dictionary
		mapping int to Student.		
		"""
		result = f'{self.course}\n'
		for student in self.students.values():
			result += student.__str__()
		return result
