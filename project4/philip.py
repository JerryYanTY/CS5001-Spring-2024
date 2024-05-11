
def convert_into_text_string(file) -> list:
    '''this function converts the file.py into a list of strings
    input: python file file.py
    output: a list'''
def sloc_total_lines(string_list) -> int:
    '''this function will returnn the total number of
    source lines in the entire list aka the list of strings
    input: file.py string_list
    output: integer of the total number of lines in the list'''

    line_count = 0
    file_lines = len(string_list)


    for line in string_list:
        if line != file_lines.startswith(''):
            line_count += 1
        else:
            file_lines += 0
    return line_count



def comment_lines(string_list) -> int:
    '''this function will count the number of comments in the file.txt
    The triple quotes will be counted as 4 lines while the hashtag will
    be counted as 1 line.
    input: file.txt
    output: integer of the number of comments"'''

    line_count = 0
    file_lines_comment = len(string_list)

    for line in file_lines_comment:
        if "'''" in line:
            line_count
        if "#" in line:
            line_count += 1
        else:
            line_count += 0
    return line_count


def function_names(string_list) -> int
'''this function will count the number of lines in the file.txt
that are a function.
input: file
output: integer of the number of lines in the file.txt that are functions'''

line_count = 0
function_lines = len(string_list)

    for line in string_list:
        if string_list.startswith('def'):
            line_count += 1
        else:
            line_count += 0
    return line_count

def lines_too_long(string_list) -> int:
    '''this function will count the number of lines in the file.txt
    that are too long (over 80 characters).
    input: file.txt
    output: integer of the number of lines that are 80 characters or more'''

    line_count = 0
    file_lines = len(string_list)

    for line in string_list:
        if len(line) >= 80:
            line_count += 1
        else:
            line_count +=
    return line_count





