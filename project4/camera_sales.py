def welcome():
    print('Welcome, user.')


def get_cameras_sold() -> int:
    return int(input('Number of cameras sold: '))


def get_camera_price() -> float:
    return float(input('The price per camera (in $): '))


def calculate_total_pay(no_sold: int, price_p_camera: float) -> float:
    return 1500+no_sold * 200 + no_sold * price_p_camera * 0.02
    # return round((1500+no_sold * 200 + no_sold * price_p_camera * 0.02), 2)


def display_total(total_pay: float):
    print(f'Your total is: ${total_pay}')


def main():
    no_sold = get_cameras_sold()
    camera_price = get_camera_price()
    total_pay = calculate_total_pay(no_sold, camera_price)
    display_total(total_pay)


if __name__ == '__main__':
    main()
