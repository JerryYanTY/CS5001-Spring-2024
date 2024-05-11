def main():
    bill_total = float(input('Enter the total bill: '))
    service_quality = str(input('Enter the quality of the service: '))
    diner_no = int(input('Enter the number of diners: '))   # getting necessary info in correct types
    if service_quality == 'fair':   # calculate total bill after tipping
        bill_total = bill_total*1.18
    elif service_quality == 'good':
        bill_total = bill_total*1.20
    elif service_quality == 'excellent':
        bill_total = bill_total*1.25
    else:
        print('Invalid input')   # exit the program if the input is not recognized
        exit()
    split_bill = round(bill_total / diner_no, 2)   # rounding up to 2 decimals
    print(f'Every diner should pay {split_bill}')   # print the result


if __name__ == '__main__':
    main()
