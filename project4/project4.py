import sys
import os


def get_name() -> str:
    """
    This helper function gets the sys.argv[1], the name of the file we want to run this program on.
    """
    try:
        return sys.argv[1]
    except IndexError as ie:
        print(ie)


def open_file(filename: str) -> list[str]:
    """
    this function converts the file.py into a list of strings.
    input: filename
    output: a list of the filename
    """
    result = []
    with open(filename, 'r') as file:
        for line in file:
            result.append(line)
    return result


def SLOC(program: list[str]) -> int:
    """
    this function will returnn the total number of source lines in the program.
    input: file.py string_list
    output: integer of the total number of lines in the list
    """
    return len(program)


def comment_lines(program: list[str]) -> int:
    """
    this function will count the number of comments in the program.
    input: program
    output: integer of the number of comments
    """
    comment_flag = False
    count = 0
    for line in program:
        line = line.lstrip()
        if line.startswith('#'):
            count += 1
        elif line.startswith('\'\'\''):
            if comment_flag:
                comment_flag = False
            else:
                comment_flag = True
        elif line.startswith('\"\"\"'):
            if comment_flag:
                count += 1
                comment_flag = False
            else:
                comment_flag = True
        if comment_flag:
            count += 1
    return count


def name_string(raw: str):
    """
    Helper Function to strip raw string and return only the second part,
    which is the function name, of it.
    input: raw string
    """
    result = raw.split()
    raw = result[1]
    re = ''
    for item in raw:
        if item != '(':
            re += item
        else:
            break
    return re


def function_names(program: list[str]) -> list[str]:
    """
    this function will return a list of function names found in the program
    input: program
    output: a list of function names
    """
    result = []
    for line in program:
        line = line.lstrip()
        if line.startswith('def'):
            result.append(name_string(line))
    return result


def long_lines(program: list[str]) -> list[int]:
    """
    this function will count the number of lines in the program file
    that are over 80 characters.
    input: program
    output: a list of integers indicating which lines are over 80 characters
    """
    result = []
    for line in program:
        if len(line) > 80:
            result.append(program.index(line) + 1)
    return result


def no_docstring(program: list[str]) -> list[str]:
    """
    this function will return a list of functions that do not have a docstring
    input: program
    output: list of functions that do not have a docstring
    """
    line = 0
    wo_doc = []
    while line < len(program):
        curr = program[line].lstrip()
        if curr.startswith('def'):
            function = name_string(program[line])
            if '\"\"\"' not in program[line + 1] and '\'\'\'' not in program[line + 1]:
                wo_doc.append(function)
        line += 1
    return wo_doc


def get_indentation(line: str) -> int:
    '''
    this helper function will determine the amount of indentation at the beginning
    of a line
    input: line
    output: an int of the indentation tabs
    '''
    orig = len(line)
    line = line.lstrip()
    curr = len(line)
    return orig - curr


def long_functions(program: list[str]) -> list[str]:
    """
    this function will return a list of function names that exceed 40 lines of code.
    input: program
    output: list of function names that exceed 40 lines
    """
    function_flag = False
    long_f = []
    line_count = 0
    f_len_mark = 0
    function = ''
    for line in program:
        indent = get_indentation(line)
        if indent <= f_len_mark and function_flag:
            line_count = 0
            function_flag = False
        if line.startswith('def') and not function_flag:
            function = name_string(line)
            function_flag = True
            f_len_mark = indent
        if function_flag:
            line_count += 1
        if line_count > 40:
            long_f.append(function)
            function_flag = False
            line_count = 0
    return long_f


def superf_parens(program: list[str]) -> list[int]:
    """
    this function will return a list of integers representing the lines
    where a superfluous parenthesis occurs.
    input: program
    output: a list of integers representing indicating what line the superfluous parenthesis are in
    """
    result = []
    line = 0
    while line < len(program):
        curr = program[line]
        curr = curr.replace(' ', '')
        if ('if(' in curr or 'while(' in curr or 'for(' in curr) and ':' in curr:
            result.append(line + 1)
        line += 1
    return result


def function_uncalled(program: list[str]) -> list[str]:
    """
    This function returns a list of functions which are never called.
    input: program
    output: a list of uncalled functions
    """
    all_func_names = function_names(program)
    uncalled_func = []
    for name in all_func_names:
        count = 0
        for line in program:
            if name in line:
                if name + '(' not in line and not line.startswith(name):
                    count += 1
        if count == 1:
            uncalled_func.append(name)
    return uncalled_func


def single_char(program: list[str]) -> list[str]:
    """
    This function returns a list of variables of size 1.
    input: program
    output: a list of single-char variables
    """
    result = []
    for line in program:
        if '=' in line:
            pos = line.find('=')
            temp = line[:pos]
            temp = temp.replace(' ', '')
            if len(temp) == 1 and temp not in result:
                result.append(temp)
    return result


def main():
    """
    this function runs the program to fulfill the project 4 requirements
    input:
    output:
    """
    name = get_name()
    print(name)
    program = open_file(name)
    print(program)
    print(f'SLOC:{len(program)}')
    print(f'Comment Lines: {comment_lines(program)}')
    functions = function_names(program)
    if functions:
        print('Function Names:')
        for function in functions:
            print('    ' + function)
    else:
        print('No functions.')
    longs = long_lines(program)
    if longs:
        print(f'Lines Too Long: \n    {longs}')
    else:
        print('No Lines Are Too Long.')
    func_no_doc = no_docstring(program)
    if func_no_doc:
        print('Missing Function Docstring: ')
        for function in func_no_doc:
            print('    ' + function)
    else:
        print('All Functions Have A Docstring.')
    long_func = long_functions(program)
    if long_func:
        print('Functions Too Long: ')
        for func in long_func:
            print('    ' + func)
    else:
        print('All Functions Are Of Good Lengths.')
    unnec_paren = superf_parens(program)
    if unnec_paren:
        print('Superfluous Parens: ')
        print('    ', end='')
        print(unnec_paren)
    else:
        print('There is no superfluous Parens.')
    uncalled = function_uncalled(program)
    if uncalled:
        print('Functions That Are Never Called:')
        for item in uncalled:
            print('    ' + item)
    singles = single_char(program)
    if singles:
        print('Single-char Variables: ')
        for item in singles:
            print('    ' + item)


if __name__ == '__main__':
    main()
