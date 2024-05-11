def main():
    print("Welcome tp Small Business Owner's name's store!\nWe offer item 1, item 2, and item 3.")
    no_1 = int(input('How many item 1s would you like ($1.50/item)? '))
    no_2 = int(input('How many item 2s would you like ($3/item)? '))
    no_3 = int(input('How many item 3s would you like ($4.55/item)? '))   # showing prompt and getting values
    bill_total = round(no_1 * 1.50 + no_2 * 3 + no_3 * 4.55,2)   # the rounding keeps remainder from storing funny
    # binary values (applicable throughout the code
    print(f"Your total is ${bill_total}")
    payment = float(input('Enter payment amount: '))
    change = round(payment - bill_total, 2)    # get the amount of change owed
    remainder = change
    if change >= 0:
        twty_bill = change // 20    # getting no of different bills/coins and calculate the remaining change owed
        remainder = round(remainder % 20, 2)
        ten_bill = remainder // 10
        remainder = round(remainder % 10, 2)
        five_bill = remainder // 5
        remainder = round(remainder % 5, 2)
        one_bill = remainder // 1
        remainder = round(remainder % 1, 2)
        qt_coin = remainder // 0.25
        remainder = round(remainder % 0.25, 2)
        dm_coin = remainder // 0.10
        remainder = round(remainder % 0.10, 2)
        nk_coin = remainder // 0.05
        remainder = round(remainder % 0.05, 2)
        py_coin = remainder / 0.01
        print(f'Your total change is ${change}\n'
              f'You are owed: \n    $20 - {twty_bill} \n    $10 - {ten_bill} \n'
              f'    $5 - {five_bill} \n    $1 - {one_bill} \n    $.25 - {qt_coin}\n'
              f'    $.10 - {dm_coin} \n    $.05 - {nk_coin} \n    $.01 - {py_coin}')    # print results

    else:
        change = 0 - change   # get the money the buy owes
        print(f'Sorry, you are ${change} short.')
        exit()      # exit and print error if the payment is insufficient


if __name__ == "__main__":
    main()
