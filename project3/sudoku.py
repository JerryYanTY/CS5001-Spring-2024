"""
Sudoku Helper
This program provides helper functions for a sudoku
game. It can check a board to determine whether the
rows, columns, and subsquares are correct. It can 
also solve a board if a solution exists.

One of the test boards was taken from
https://lipas.uwasa.fi/~timan/sudoku/s10b.txt
"""
import os

SUDOKU = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # global constant to facilitate checking


def read_board(filename: str) -> list[list[int]]:
	"""Reads a file containing a 9x9 sudoku
	board formated as nine rows of nine
	comma-separated integers. Creates a list
	containing nine lists where each list
	is a row of the text file.
	The parameter filename is the location
	of the file.
	Returns the list of lists.
	Example file text:
	0,5,0,0,1,0,0,4,0
	1,0,1,0,0,0,6,0,2
	0,0,0,9,0,5,0,0,0
	2,0,8,0,3,0,5,0,1
	0,4,0,0,7,0,0,2,0
	9,0,1,0,8,0,4,0,6
	0,0,0,4,0,1,0,0,0
	3,0,4,0,0,0,7,0,9
	0,2,0,0,6,0,0,1,0

	Expected data structure:
			[
				[0,5,0,0,1,0,0,4,0],
				[1,0,1,0,0,0,6,0,2],
				[0,0,0,9,0,5,0,0,0],
				[2,0,8,0,3,0,5,0,1],
				[0,4,0,0,7,0,0,2,0],
				[9,0,1,0,8,0,4,0,6],
				[0,0,0,4,0,1,0,0,0],
				[3,0,4,0,0,0,7,0,9],
				[0,2,0,0,6,0,0,1,0]
			]

	"""
	result = []  # to be returned
	temp = []  # temporary holder
	with open(filename, 'r') as input_file:
		for line in input_file:  # take lines
			for char in line:  # take chars in a line
				if char.isnumeric():  # check if the char is a number
					temp.append(int(char))  # put numbers in a list

			result.append(temp)  # 2d list
			temp = []  # reset temp
	return result


def check_rows(board: list[list[int]]) -> bool:
	"""Returns True if every row in the board
	data structure contains all numbers 1-9
	and False otherwise.
	"""
	for line in board:  # iterate through board
		sorted_list = sorted(line)  # sort list
		if sorted_list != SUDOKU:  # compare with the complete set
			return False
	return True


def check_columns(board: list[list[int]]) -> bool:
	"""Returns True if every column in the board
	data structure contains all numbers 1-9
	and False otherwise.
	"""
	for i in range(9):  # iterate from left to right
		sorted_list = []
		for line in board:
			sorted_list.append(line[i])
		sorted_list.sort()  # sort
		if sorted_list != SUDOKU:  # check against complete set
			return False
	return True


def check_squares(board: list[list[int]]) -> bool:
	"""Returns True if every subsquare in the board
	data structure contains all numbers 1-9
	and False otherwise.
	"""
	test_square = []
	for i in range(0, 3, 9):  # iterate with an interval of 3 from top to bot
		for j in range(0, 3, 9):  # iterate with an interval of 3 from left to right
			test_square = (board[i][j:j + 3]) + (board[i + 1][j:j + 3]) + (board[i + 2][j:j + 3])
			test_square.sort()  # sort
			if test_square != SUDOKU:  # check against the complete set
				test_square = []  # reset square holder
				return False
			else:
				test_square = []  # reset square holder
	return True


def candidate_values(board: list[list[int]],
					 row: int,
					 column: int) -> list[int]:
	"""Takes as parameters a board and two ints
	specifying the row and column of a particular
	square. Returns a list of all possible integers
	that can go in the given square.
	This function does not "look ahead". It will
	return a list of the numbers that do not appear
	in the row specified by row, nor the column
	specified by column, nor the subsquare in
	which the square is located.
	"""
	curr_row = board[row]  # get row
	curr_column = []
	for i in range(9):
		curr_column.append(board[i][column])  # get column
	curr_square = []
	x = 3 * (row // 3)
	y = 3 * (column // 3)
	curr_square = (board[x][y:y + 3]) + (board[x + 1][y:y + 3]) + (board[x + 2][y:y + 3])  # get sub square
	row_pot_val = [x for x in SUDOKU if x not in curr_row and x not in curr_column and x not in curr_square]
	# check against complete set, return the difference
	return row_pot_val


def solve(board: list[list[int]]) -> bool:
	"""Takes a board as a parameter. Returns
	True if the board can be solved and False
	if not.
	If the board can be solved then the board
	data structure will contain the solution
	when the function completes. If the board
	cannot be solved then the board will have
	all of the original data after the function
	completes.
	"""
	if check_rows(board) and check_columns(board) and check_squares(board):   # 'base case' there is a solution
		return True

	for row in range(9):
		for column in range(9):   # iterate through the board
			if board[row][column] == 0:   # find the blank
				possible = candidate_values(board, row, column)   # get the possible values
				for i in possible:   # try the values one by one
					board[row][column] = i   # assign the value to update the board
					if solve(board):   # this is the recursion
						return True   # if the recursion returns true, we have a solution
				board[row][column] = 0   # else we reset the blank
				return False   # and return false to continue trying
	return False   # is this the base case?


def main():
	# new_list = read_board('incomplete.txt')
	# print(new_list)
	# print(check_rows(new_list))
	# print(check_columns(new_list))
	# print(check_squares(new_list))
	# print(candidate_values(new_list, 0, 2))
	# print(solve(new_list))
	# print(new_list)   # testing functions
	"""ACTUAL MAIN STARTS HERE"""
	again = ''
	checkrow = ''
	checkcolumn = ''
	checksquares = ''
	solveornot = ''
	print('Hi, welcome to Sudoku!\nGive me a file and I will try to solve.')
	while again != 'no':
		filename = input('Enter the file name:')
		board = read_board(filename)
		if check_rows(board) and check_columns(board) and check_squares(board):
			print('Congratulations! Your board is a valid solution!')
		else:
			if not check_rows(board):
				checkrow = '......invalid rows'
			if not check_columns(board):
				checkcolumn = '......invalid columns'
			if not check_squares(board):
				checksquares = '......invalid subsquares'
			print(f'Sorry{checkrow}{checkcolumn}{checksquares}...')
			while solveornot != 'yes' and solveornot != 'no':
				solveornot = input('Would you like me to solve this for you?')
			if solveornot == 'yes':
				if solve(board):
					print('Yay!I found a solution!')
					for row in board:
						for column in row:
							print(column, end='')
						print('\n', end='')
				else:
					print('Sorry, no solution.')
		while again != 'no' and again != 'yes':
			again = input('Would you like to go again?')


if __name__ == '__main__':
	main()
