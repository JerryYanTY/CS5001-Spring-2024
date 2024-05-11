OZ = 28
CUP = 250
TEAS = 5
TABLES = 15


def get_ingredients() -> str:  # gets name of ingredient
    return input('Which ingredient does your recipe call for? ')


def get_amount_avail(ingredient: str) -> list:  # gets amount and unit of available ingredient -> a list
    return list(input(f'How much {ingredient} do you have on hand? ').split(' '))


def get_amount_needed(ingredient: str) -> list:  # gets amount and unit of needed ingredient -> a list
    return list(input(f'How much {ingredient} do you need? ').split(' '))


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
        result.append('Invalid measurement.')       # in the case of invalid units
    return result


def check_input(need_converted: list) -> bool:      # works with the previous function to test the validity of inputs
    if len(need_converted) == 1:
        return False
    return True


def need_amount(ingre: str, need_converted: list) -> str:       # returns a printable string
    return f'You need {need_converted[0]} {need_converted[1]} of {ingre}'


def comparison(have: list, need_converted: list) -> bool:       # checks if we have enough
    available_amount = float(have[0])
    needed_amount = float(need_converted[0])
    if available_amount > needed_amount:
        return True
    return False


def final_remark(ingre: str, enough: bool) -> str:          # returns a printable string that matches the comparison
    if enough:
        return 'It looks like you can make your recipe!'
    return f'Sorry, you don\'t have enough {ingre}.'


def welcome() -> str:   # this function gives a printable welcoming message
    return ('Welcome to the recipe helper? \n I can help you convert US standard measurements'
            ' to metric.'
            '\n You tell me the US standard amount of the ingredient you have on hand,'
            '\n And I\'ll tell you whether you have enough to make your recipe'
            '\n specified in metric.'
            '\n'
            '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            '\n')


def main():
    print(welcome())  # print welcoming message
    ingre = get_ingredients()  # get the ingredient name
    have = get_amount_avail(ingre)  # get the amount we have, and store no.&unit in a list
    need = get_amount_needed(ingre)  # get the amount we need. and store no.&unit in a list
    need_converted = metric_to_us(have, need)  # store the converted no.&unit
    if check_input(need_converted):
        print(need_amount(ingre, need_converted))  # print needed amount
        print(final_remark(ingre, comparison(have, need_converted)))  # print final judgment based on comparison
    else:
        print(*need_converted)        # in the case that invalid inputs are received
        exit()


if __name__ == '__main__':
    main()
