import math


def changeNumber(n, k):
    result = ""
    while n > 0:
        result += str(n % k)
        n //= k
    return result[::-1]


def isPrime(n):
    if n == 1: return False
    if n == 2: return True

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False

    return True


def solution(n, k):
    answer = 0
    number = changeNumber(n, k)

    numbers = [s for s in number.split('0') if s != '']

    for n in numbers:
        if isPrime(int(n)): answer += 1

    return answer