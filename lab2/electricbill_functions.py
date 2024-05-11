def electric_bill(base_rate: float, kwh_used: float) -> float:
    if kwh_used > 1000 and base_rate > 0:  # case when more than 1000 kWh are used
        total_price = round(1000 * base_rate + (kwh_used - 1000) * (base_rate * 1.25), 2)  # calculation
        return total_price   # return a value
    elif kwh_used >= 0 and base_rate > 0:  # case when fewer than 1000 kWh are used
        total_price = round(kwh_used * base_rate, 2)  # calculation and get up to two decimals (cent)
        return total_price
    else:
        print('Invalid input')  # when the input is not possible


def main():
    money = electric_bill(2.45, 4000)  # an example of calling the function
    print(money)


if __name__ == '__main__':
    main()
