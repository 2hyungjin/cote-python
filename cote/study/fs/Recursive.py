def rec(i):
    if i == 10: return
    print(f"{i}에서 {i + 1}호출")
    rec(i + 1)
    print(f"{i} 종료")


def fac(n):
    if n == 1: return 1
    return n * fac(n - 1)


def uclid(n, m):
    _m = min(n, m)
    _n = max(n, m)
    if _n % _m == 0: return _m
    else: return uclid(_m, _n % _m)


if __name__ == '__main__':
    print(uclid(192,162))
