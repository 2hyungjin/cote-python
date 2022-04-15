def dp(array, n):
    d = [0] * 100
    d[0] = array[0]
    d[1] = max(d[0], d[1])
    for i in range(0, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])
    print(d[i])


if __name__ == '__main__':
    dp([1, 3, 3, 8], 4)
