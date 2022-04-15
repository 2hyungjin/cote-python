def dp(n, m, moneys):
    d = [-1] * 10001
    moneys.sort()
    for i in moneys: d[i] = 1

    for i in range(2, m + 1):
        for money in moneys:
            if i > money and d[i - money] > 0:
                if d[i] > 0:
                    d[i] = min(d[i], d[i - money] + 1)
                else:
                    d[i] = d[i - money] + 1
    return d[m]


if __name__ == '__main__':
    n, m = map(int, input().split())
    moneys=[]
    for i in range(n):
        moneys.append(int(input()))
    print(dp(n, m, moneys))
