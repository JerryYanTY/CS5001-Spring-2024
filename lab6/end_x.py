def endX(s: str) -> str:
    if len(s) == 0:
        return ''   # the original string is gone over
    if s[0] == 'x':
        return endX(s[1:])+'x'   # if the first char is 'x', append it to the end of our returned string
    else:
        return s[0]+endX(s[1:])   # if the first char is not 'x', append to the beginning


def main():
    print(endX('xhixhix'))
    print(endX('xxre'))
    print(endX('xxhixx'))


if __name__ == '__main__':
    main()
