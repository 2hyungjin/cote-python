def dp(n):
    d = [0] * 99999

    for i in range(2, n + 1):
        d[i] = d[i - 1]+1

        if i % 5 == 0:
            d[i] = min(d[i // 5] + 1,d[i])
        if i % 3 == 0:
            d[i] = min(d[i // 3] + 1,d[i])
        if i % 2 == 0:
            d[i] = min(d[i // 2] + 1,d[i])

    for i in range(1, n + 1):
        print(i, d[i])
    return d[i]


if __name__ == '__main__':
    print(dp(10))
