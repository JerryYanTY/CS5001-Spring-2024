def count_ing_words() -> int:
    word = 'PLACEHOLDER'        # initialize a string object
    count = 0                   # to be returned
    while not word == 'quit':           # check the word
        word = input('Enter next word -- use \'quit\' to end input:  ').lower()      # turn the word into all lowercases
        if word.endswith('ing'):        # check word's ending
            count += 1                  # update count
    return count


def main():
    count = count_ing_words()
    print(f'You entered {count} words ending with \'ing\'')


if __name__ == '__main__':
    main()
