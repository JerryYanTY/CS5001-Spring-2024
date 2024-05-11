def main():
    card_rank = str(input("Enter card rank: "))   # getting card rank
    card_value = 0   # default card value
    if card_rank == 'Joker':   # converting card rank to value
        card_value = 50
    elif card_rank == 'Two' or card_rank == 'Ace':
        card_value = 20
    elif card_rank == 'Nine' or card_rank == 'Ten' or \
            card_rank == 'Jack' or card_rank == 'Queen' or \
            card_rank == 'King':
        card_value = 10
    elif card_rank == 'Four' or card_rank == 'Five' or \
            card_rank == 'Six' or card_rank == 'Seven' or \
            card_rank == 'Eight':
        card_value = 5
    elif card_rank == 'Three':   # special case
        three_color = str(input('Enter the color of the card:'))
        if three_color == 'Black':
            card_value = 5
        elif three_color == 'Red':
            card_value = 0
        else:
            print('Invalid color')
            exit()   # exit to prevent from printing anything
    else:
        print('Invalid rank')
        exit()   # exit to prevent from printing anything
    print(f'The card value is {card_value}.')   # print output


if __name__ == '__main__':
    main()
