def main():
    total_price = 0  # create a global variable to store total amount due
    kwh_month = float(input('Enter the number of kWh you have used in the past month: '))  # get number of kWh
    price_per_kwh = float(input('Enter the base kWh price: '))  # get base price
    if kwh_month > 1000:  # case when more than 1000 kWh are used
        total_price = 1000 * price_per_kwh + (kwh_month - 1000) * (price_per_kwh * 1.25)  # calculation
    elif kwh_month >= 0:  # case when fewer than 1000 kWh are used
        total_price = kwh_month * price_per_kwh   # calculation and get to only the second decimal(cent)
    else:
        print('Invalid input')  # when the input is not possible
        exit()
    round(total_price, 2)    # round to cent to reflect real-life scenario
    print(f'The total amount due is ${total_price}')  # print results


if __name__ == '__main__':
    main()
