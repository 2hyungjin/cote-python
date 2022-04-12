if __name__ == '__main__':
    s = input()
    number = 0
    alphabet = []
    for c in s:
        if c.isnumeric(): number += int(c)
        if c.isalpha(): alphabet += c
    alphabet.sort()

    print(''.join(alphabet) + str(number))
