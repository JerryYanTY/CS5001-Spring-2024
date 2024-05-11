def welcome():      # print a welcoming message
    print('Welcome, user.')


def get_cameras_sold() -> int:      # get the no. of cameras sold
    return int(input('Number of cameras sold: '))


def get_camera_price() -> float:        # get the price of one camera
    return float(input('The price per camera (in $): '))


def calculate_total_pay(no_sold: int, price_p_camera: float) -> float:      # calculate the salary
    return 1500+no_sold * 200 + no_sold * price_p_camera * 0.02
    # return round((1500+no_sold * 200 + no_sold * price_p_camera * 0.02), 2)


def display_total(total_pay: float):        # print out the salary
    print(f'You have earned ${total_pay} this month!')


def main():     # calling the functions
    no_sold = get_cameras_sold()
    camera_price = get_camera_price()
    total_pay = calculate_total_pay(no_sold, camera_price)
    display_total(total_pay)


if __name__ == '__main__':
    main()
