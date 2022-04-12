if __name__ == '__main__':
    s = input()
    result = 0
    for c in s:
        if c == '0' or c == '1' or result == 0:
            result += int(c)
        else:
            result *= int(c)
    print(result)
