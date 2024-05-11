import random
# 1 = rock  2 = paper  3 = scissors
# 1 beats 3, 2 beats 1, 3 beats 2


def pc_choice() -> int:   # getting a pc generated choice and return as an int
    return random.randint(1,3)


def player_choice() -> int:     # convert user input to int, if not valid, return -1
    choice = input('Enter your choice: ')
    if choice == 'rock':
        return 1
    elif choice == 'paper':
        return 2
    elif choice == 'scissors':
        return 3
    else:
        return -1


def check_input(player_input: int) -> bool:     # check if the user's input is valid
    if player_input < 0:
        return False
    return True


def check_winner(player_input: int, pc_input: int) -> str:   # check who wins and return the winner(or draw)
    if player_input == pc_input:
        return 'No one'
    elif (player_input > 1 and pc_input == (player_input-1)) or (player_input == 1 and pc_input == 3):
        return 'The player'
    else:
        return 'The computer'


def main():     # calling the functions to play the game
    pc_rps = pc_choice()
    user_rps = player_choice()
    if check_input(user_rps):
        print(f'{check_winner(pc_rps, user_rps)} wins')
    else:
        print('Invalid input')
        exit()


if __name__ == '__main__':
    main()
