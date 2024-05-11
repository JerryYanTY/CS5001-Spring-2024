def passwordify(original: str) -> str:
    original = original.replace('s', '$').replace('S', '$')   # changing s and S
    original = original.replace('l', '1').replace('L', '1')   # changing l and L
    original = original.replace(' ', '-')                                 # changing ' '
    original = original.replace('zero', '0').replace('one', '1').replace(
        'two', '2').replace('three', '3').replace('four', '4').replace(
        'five', '5').replace('six', '6').replace('seven', '7').replace(
        'eight', '8').replace('nine', '9').replace('ten', '10')
    # changing 'numbers'
    return original


def main():
    original = input('Enter a string: ')
    print(passwordify(original))


if __name__ == '__main__':
    main()
