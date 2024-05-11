def find_greater(values: list[int], target: int) -> int:
    count = 0       # create a count to be returned
    for item in values:     # loop through values
        if item > target:       # compare
            count += 1          # update count
    return count                # return


def main():
    values = [-8,56,89,1,2,3,4,-1.0]
    print(find_greater(values, -1))


if __name__ == '__main__':
    main()
