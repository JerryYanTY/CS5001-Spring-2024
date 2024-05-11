# import sys
# import os
#
#
# def get_name() -> str:
#     try:
#         return sys.argv[1]
#     except IndexError as ie:
#         print(ie)
#
#
# def open_file(filename: str) -> list[str]:
#     result = []
#     with open(filename, 'r') as file:
#         for line in file:
#             result.append(line)
#     return result
#
#
# def SLOC(program: list[str]) -> int:
#     return len(program)
#
#
# def comment_lines(program: list[str]) -> int:
#     # line = 0
#     # while line < len(program):
#     #     if '#' in program[line]:
#     #         count += 1
#     #         line += 1
#     #     elif '\'\'\'' in program[line]:
#     #         count += 1
#     #         line += 1
#     #         while '\'\'\'' not in program[line]:
#     #             count += 1
#     #             line += 1
#     #         count += 1
#     #         line += 1
#     #     elif '\"\"\"' in program[line]:
#     #         count += 1
#     #         line += 1
#     #         while '\"\"\"' not in program[line]:
#     #             count += 1
#     #             line += 1
#     #         count += 1
#     #         line += 1
#     #     else:
#     #         line += 1
#     comment_flag = False
#     count = 0
#     for line in program:
#         line = line.lstrip()
#         if line.startswith('#'):
#             count += 1
#         elif line.startswith('\'\'\''):
#             if comment_flag:
#                 comment_flag = False
#             else:
#                 comment_flag = True
#         elif line.startswith('\"\"\"'):
#             if comment_flag:
#                 count += 1
#                 comment_flag = False
#             else:
#                 comment_flag = True
#         if comment_flag:
#             count += 1
#     return count
#
#
# def name_string(raw: str):
#     result = raw.split()
#     raw = result[1]
#     re = ''
#     for item in raw:
#         if item != '(':
#             re += item
#         else:
#             break
#     return re
#
#
# def function_names(program: list[str]) -> list[str]:
#     result = []
#     for line in program:
#         line = line.lstrip()
#         if line.startswith('def'):
#             result.append(name_string(line))
#     return result
#
#
# def long_lines(program: list[str]) -> list[int]:
#     result = []
#     for line in program:
#         if len(line) > 80:
#             result.append(program.index(line) + 1)
#     return result
#
#
# def no_docstring(program: list[str]) -> list[str]:
#     line = 0
#     wo_doc = []
#     while line < len(program):
#         curr = program[line].lstrip()
#         if curr.startswith('def'):
#             function = name_string(program[line])
#             if '\"\"\"' not in program[line + 1] and '\'\'\'' not in program[line + 1]:
#                 wo_doc.append(function)
#         line += 1
#     return wo_doc
#
#
# def get_indentation(line: str) -> int:
#     orig = len(line)
#     line = line.lstrip()
#     curr = len(line)
#     return orig-curr
#
#
# def long_functions(program: list[str]) -> list[str]:
#     function_flag = False
#     long_f = []
#     line_count = 0
#     f_len_mark = 0
#     function = ''
#     for line in program:
#         indent = get_indentation(line)
#         if indent <= f_len_mark and function_flag:
#             line_count = 0
#             function_flag = False
#         if line.startswith('def') and not function_flag:
#             function = name_string(line)
#             function_flag = True
#             f_len_mark = indent
#         if function_flag:
#             line_count += 1
#         if line_count > 40:
#             long_f.append(function)
#             function_flag = False
#             line_count = 0
#     return long_f
#     # while line < len(program):
#     #     curr = program[line].lstrip()
#     #     if curr.startswith('def'):
#     #         function = name_string(program[line])
#     #         line_count += 1
#     #         line += 1
#     #         while not program[line].lstrip().startswith('def') and line < len(program)-1:
#     #             line_count += 1
#     #             line += 1
#     #         line_count -= 1
#     #         line -= 1
#     #         if line_count > 40:
#     #             long_f.append(function)
#     #         line_count = 0
#     #     line += 1
#
#
# def superf_parens(program: list[str]) -> list[int]:
#     result = []
#     line = 0
#     while line < len(program):
#         curr = program[line]
#         curr = curr.replace(' ', '')
#         if ('if(' in curr or 'while(' in curr or 'for(' in curr) and ':' in curr:
#             result.append(line + 1)
#         line += 1
#     return result
#
#
# def main():
#     name = get_name()
#     print(name)
#     program = open_file(name)
#     print(program)
#     print(f'SLOC:{len(program)}')
#     print(f'Comment Lines: {comment_lines(program)}')
#     functions = function_names(program)
#     if functions:
#         print('Function Names:')
#         for function in functions:
#             print('    ' + function)
#     else:
#         print('No functions.')
#     longs = long_lines(program)
#     if longs:
#         print(f'Lines Too Long: \n    {longs}')
#     else:
#         print('No Lines Are Too Long.')
#     func_no_doc = no_docstring(program)
#     if func_no_doc:
#         print('Missing Function Docstring: ')
#         for function in func_no_doc:
#             print('    ' + function)
#     else:
#         print('All Functions Have A Docstring.')
#     long_func = long_functions(program)
#     if long_func:
#         print('Functions Too Long: ')
#         for func in long_func:
#             print('    ' + func)
#     else:
#         print('All Functions Are Of Good Lengths.')
#     unnec_paren = superf_parens(program)
#     if unnec_paren:
#         print('Superfluous Parens: ')
#         print('    ', end='')
#         print(unnec_paren)
#     else:
#         print('There is no superfluous Parens.')
#
#
# if __name__ == '__main__':
#     main()
