OZ = 28
CUP = 250
TEAS = 5
TABLES = 15
ACCEPTABLE_UNIT_HAVE = ['teaspoon', 'teaspoon', 'tablespoon', 'tablespoons', 'cup', 'cups', 'ounce', 'ounces']
ACCEPTABLE_UNIT_NEED = ['ml', 'grams']


def get_ingredients() -> str:  # gets name of ingredient
    return input('Which ingredient does your recipe call for? ')


def avail_check(have: list) -> bool:
    return len(have) == 2 and have[0].isdigit() and have[1] in ACCEPTABLE_UNIT_HAVE   # check if the first input
    # unit+amount is valid
    # str.isdigit() learned from https://docs.python.org/3/library/stdtypes.html#string-methods


def need_check(need: list) -> bool:
    return len(need) == 2 and need[0].isdigit() and need[1] in ACCEPTABLE_UNIT_NEED   # check if the second input
    # unit+amount is valid


def get_amount_avail(ingredient: str) -> list:  # gets amount and unit of available ingredient -> a list
    result = list(input(f'How much {ingredient} do you have on hand? ').split(' '))
    while not avail_check(result):  # prompt the user to input the needed amount until it is accepted
        print('Invalid measurement. Please try again.')
        result = list(input(f'How much {ingredient} do you have on hand? ').split(' '))  # get the amount we need.
        # and store no.&unit in a list
    return result


def get_amount_needed(ingredient: str) -> list:  # gets amount and unit of needed ingredient -> a list
    result = list(input(f'How much {ingredient} do you need? ').split(' '))
    while not need_check(result):  # prompt the user to input the needed amount until it is accepted
        print('Invalid measurement. Please try again.')
        result = list(input(f'How much {ingredient} do you need? ').split(' '))  # get the amount we need.
        # and store no.&unit in a list
    return result


def metric_to_us(have: list, need: list) -> list:  # converts needed to US standard -> a list, also serves as
    # a checking function, if the resulting list has only 1 item, the inputs are invalid
    result = []
    if (have[1] == 'teaspoon' or have[1] == 'teaspoons') and need[1] == 'ml':
        result.append(float(need[0]) / TEAS)  # needed ingre ml -> teaspoons
        result.append('teaspoons')
    elif (have[1] == 'tablespoon' or have[1] == 'tablespoons') and need[1] == 'ml':
        result.append(float(need[0]) / TABLES)  # needed ingre ml -> tablespoons
        result.append('tablespoons')
    elif (have[1] == 'cup' or have[1] == 'cups') and need[1] == 'ml':
        result.append(float(need[0]) / CUP)  # needed ingre ml -> cups
        result.append('cups')
    elif (have[1] == 'ounce' or have[1] == 'ounces') and need[1] == 'grams':
        result.append(float(need[0]) / OZ)  # needed ingre gram -> OZ
        result.append('ounces')
    else:
        result.append('Units do not match. Please enter again.')  # in the case of unmatchable units
    return result


def check_output(need_converted: list) -> bool:  # works with the previous function to test the validity of inputs
    if len(need_converted) == 1:
        return False
    return True


def need_amount(ingre: str, need_converted: list) -> str:  # returns a printable string
    return f'You need {need_converted[0]} {need_converted[1]} of {ingre}'


def comparison(have: list, need_converted: list) -> bool:  # checks if we have enough
    available_amount = float(have[0])
    needed_amount = float(need_converted[0])
    if available_amount > needed_amount:
        return True
    return False


def final_remark(ingre: str, enough: bool) -> str:  # returns a printable string that matches the comparison
    if enough:
        return 'It looks like you can make your recipe!'
    return f'Sorry, you don\'t have enough {ingre}.'


def welcome() -> str:  # this function gives a printable welcoming message
    return ('Welcome to the recipe helper? \n I can help you convert US standard measurements'
            ' to metric.'
            '\n You tell me the US standard amount of the ingredient you have on hand,'
            '\n And I\'ll tell you whether you have enough to make your recipe'
            '\n specified in metric.'
            '\n'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '\n')


def quit_check(quit_word: str) -> bool:
    return quit_word == 'yes'   # check user's input to decide whether to quit


def get_quit() -> str:
    return input('Do you wish to quit? (yes/no)')   # prompt user to input whether he/she want to quit


def main():
    print(welcome())  # print welcoming message
    quitting = ''
    while not quit_check(quitting):
        ingre = get_ingredients()  # get the ingredient name
        have = get_amount_avail(ingre)  # get the initial input of available ingredient
        need = get_amount_needed(ingre)   # get the initial input of needed ingredient
        need_converted = metric_to_us(have, need)  # store the converted no.&unit
        while not check_output(need_converted):   # while the input units are not matched, prompt user to redo
            print(*need_converted)
            have = get_amount_avail(ingre)
            need = get_amount_needed(ingre)
            need_converted = metric_to_us(have, need)  # in the case that unconvertible units are received
        print(need_amount(ingre, need_converted))  # print needed amount
        print(final_remark(ingre, comparison(have, need_converted)))  # print final judgment based on comparison
        quitting = get_quit()   # check if the user wants to quit
    exit()


if __name__ == '__main__':
    main()
