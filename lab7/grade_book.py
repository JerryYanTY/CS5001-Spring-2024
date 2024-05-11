def grade_book_entry() -> dict:
    book = {}   # initialize empty dictionary
    stop_entry = False   # setting stop-indicator to false
    entry = ''   # initialize temporary string holder for names
    while not stop_entry:   # while loop to take in one name and its scores at a time
        entry = input('What is the name of the next student? ')

        if entry in book:
            grades = book[entry]
        else:
            grades = []
            book[entry] = grades

        grade = input(f'Enter next score for {entry} or -1 to end input: ')
        while grade != '-1':
            try:
                grade = float(grade)
                grades.append(grade)
            except ValueError as TE:
                print('Scores must be floating point numbers.')

            grade = input(f'Enter next score for {entry} or -1 to end input: ')

        stop_entry = check_reentry()   # until 'quit' is called

    return book


def check_reentry():   # ask the user whether to continue input students' grades
    reentry = input('Would you like to record scores for another student? (y/n) ')
    while reentry != 'y' and reentry != 'n':
        print('Invalid input. Answer must be y or n.')
        reentry = input('Would you like to record scores for another student? (y/n) ')
    return reentry == 'n'


def print_grade(gb: dict):
    for name in gb:
        print(name)  # print name
        for item in gb[name]:
            print(item, ' ', end='')   # and corresponding scores
        print('\n')


def grade_book():
    gb = grade_book_entry()
    print_grade(gb)


def main():
    grade_book()


if __name__ == '__main__':
    main()
