def sum_before(n: list[int]) -> bool:
    if len(n) <= 2 and n[0] != n[1]:   # if the final two numbers (prev. sum and last no.) are different, return false
        return False
    if n[0] == n[1]:   # if the first two numbers (prev. sum and last no.) are the same, return true
        return True
    n[0] = n[0] + n[1]   # sum up the first two no.
    n.pop(1)   # remove the second number
    return sum_before(n)   # recursively call the function


def main():
    print(sum_before([1, 2, 5, 2, 10]))


if __name__ == '__main__':
    main()
