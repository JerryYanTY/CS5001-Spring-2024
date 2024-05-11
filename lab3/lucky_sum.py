def lucky_sum(a: int, b: int, c: int) -> int:
    if a == 13:  # 1st int being 13 means no int would count towards a sum
        return 0
    elif b == 13:  # checking from left to right and return sum accordingly
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c  # no 13 means sum of a, b and c


def main():
    # 5 cases in which different numbers of 13/
    # and positions are tested
    num = lucky_sum(5, 5, 5)
    print(num)
    num = lucky_sum(13, 1, 1)
    print(num)
    num = lucky_sum(1, 13, 1)
    print(num)
    num = lucky_sum(1, 1, 13)
    print(num)
    num = lucky_sum(13, 2, 13)
    print(num)


if __name__ == '__main__':
    main()
