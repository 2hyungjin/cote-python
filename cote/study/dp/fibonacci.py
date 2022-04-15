d = [0] * 100


# top down
def fibo(x):
    if x == 1 or x == 2: return 1
    if d[x] != 0: return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


# bottom up
def fibo2(x):
    d[1], d[2] = 1, 1
    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[x]


if __name__ == '__main__':
    print(fibo2(99))
