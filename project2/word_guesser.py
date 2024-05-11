import random  # library required to randomly choose a secret word
from colorama import Fore  # library for colored output


def get_secret_word() -> str:
    """Returns a randomly generated secret word.
    Uses the list of words in the public domain retrieved from:
    https://www-cs-faculty.stanford.edu/~knuth/sgb.html
    Requires a text file called words.txt.
    """
    with open('words.txt') as f:
        words = f.read().splitlines()
        word = random.choice(words)
    return word


class Wordle:
    secret = ''  # initialize default private members
    guess = ''
    color = []  # this is where the color of each letter is stored
    win_count = 0  # no of wins
    lose_count = 0  # no of losses
    guess_count = 0  # no of guesses
    quit = False  # default boolean value to see if the user wanna quit

    def __init__(self, s, g):  # initialize function (though later in the code I didn't use this method)
        self.secret = s
        self.guess = g

    '''I could have written a function to get the secret word, but it's just one line so no point.'''

    def get_guess(self):  # prompt user to input a guess and then convert it to lower case
        self.guess = input('Guess a word: ').lower()

    def check_length(self):  # check if the entered guess is acceptable (though it doesn't check for number input)
        while not len(self.guess) == 5:
            print('Your guess must be five characters long! Try again.')
            self.get_guess()
        print(f'You guessed {self.guess}')

    def color_update(self):  # update the color list for later use
        self.color = ['-', '-', '-', '-', '-']
        color_guess = list(self.guess)
        color_secret = list(self.secret)
        for i in range(len(color_secret)):  # check exact matches first
            for j in range(len(color_guess)):
                if color_secret[i] == color_guess[j] and i == j:
                    self.color[j] = color_guess[j] = color_secret[i] = 'G'
        for i in range(len(color_secret)):  # check right letters in wrong locations
            for j in range(len(color_guess)):
                if color_secret[i] == color_guess[j] and not color_secret[i] == 'G' \
                        and not color_secret[i] == 'Y':
                    self.color[j] = color_guess[j] = color_secret[i] = 'Y'

    def check_result(self):  # check if the user wins
        if self.guess == self.secret:
            return True
        return False

    def print_result(self):  # print out the chunk of result after each try
        if self.check_result():
            print('You win!')  # when the user got it right
            self.win_count += 1
        else:
            print('Not quite: ')  # when the user is wrong
            print(f'              {self.guess}')
            print('             ', end=' ')
            for item in self.color:  # coloring 'Y' and 'G'
                if item == 'Y':
                    print(Fore.YELLOW + item, end='')
                    print(Fore.RESET, end='')
                elif item == 'G':
                    print(Fore.GREEN + item, end='')
                    print(Fore.RESET, end='')

                else:
                    print(item, end='')
                    print(Fore.RESET, end='')

            print('\n              ', end='')
            # print(f'\n              {self.guess}')
            for i in range(len(self.color)):  # coloring 'guess'
                if self.color[i] == 'Y':
                    print(Fore.YELLOW + self.guess[i], end='')
                    print(Fore.RESET, end='')
                elif self.color[i] == 'G':
                    print(Fore.GREEN + self.guess[i], end='')
                    print(Fore.RESET, end='')
                else:
                    print(self.guess[i], end='')
                    print(Fore.RESET, end='')
            print('\n', end='')

    def quit_game(self):  # prompt the user to either quit or continue
        user_quit = input('Would you like to play again?').lower()
        while not user_quit == 'yes' and not user_quit == 'no':
            user_quit = input('Invalid input, try again: ')
        if user_quit == 'no':
            self.quit = True
        else:
            return

    def play(self):
        while not self.quit:  # while the user does not specify to quit
            self.secret = get_secret_word()  # get a secret word
            self.get_guess()  # get user's guess
            self.check_length()  # check the validity of the guess
            self.color_update()  # update color list
            # print(self.color)  # this is for testing and debugging
            self.print_result()  # print the result of first try
            self.guess_count += 1  # update the no of guesses
            while not self.check_result() and self.guess_count < 5:
                # if the user does not win and still have tries left, continue to play, up to 5 tries
                self.get_guess()
                self.check_length()
                self.color_update()
                # print(self.color)   # this is for testing and debugging
                self.print_result()
                self.guess_count += 1   # update no of tries
            if not self.check_result() and self.guess_count == 5:  # this is the case where the user loses
                self.lose_count += 1   # update mo of losses
                print(f'Sorry, you did not guess the secret word. The word was {self.secret}.')
            self.guess_count = 0   # reset no of tries
            self.quit_game()   # prompt the user to choose to quit or not
        print(f'Result - Wins: {self.win_count} | Losses: {self.lose_count}')   # if user quits, give a summary
        exit()   # exit the game


def main():
    game = Wordle('', '')  # initialize a game
    game.play()  # let it play


if __name__ == '__main__':
    main()
