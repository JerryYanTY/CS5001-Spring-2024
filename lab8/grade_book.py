from student import Student
from student_list import Student_List


def add_scores() -> bool:
    add = ''
    while add != 'n' and add != 'y':
        add = input('Would you like to record scores for another student? (y/n) ')
    return add == 'y'


def enter_scores() -> list:
    score = 0
    scores = []
    while True:
        score = input('Enter student\'s score: ')
        try:
            score = float(score)
            if score == -1:
                break
            scores.append(score)
        except ValueError:
            print('Invalid datatype. Try again.')

    return scores


def available_scores() -> bool:
    available = ''
    while available != 'y' and available != 'n':
        available = input('Would you like to record available scores? (y/n) ')
    return available == 'y'


def add_student_list():
    course = input('Please enter the name of the course: ')
    students = Student_List(course)
    return students


def add_student_info():
    name = input('Please enter the name of the student: ')
    id = input('Please enter the id of the student: ')
    scores = []
    if available_scores():
        scores = enter_scores()
    student = Student(name, id, scores)
    return student


def main():
    print('Welcome to the Student List!')
    new_sl = add_student_list()
    new_student = add_student_info()
    new_sl.add_student(new_student)
    while add_scores():
        new_student = add_student_info()
        new_sl.add_student(new_student)
    print(new_sl)


if __name__ == '__main__':
    main()
