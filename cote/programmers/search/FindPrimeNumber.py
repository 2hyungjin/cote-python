import itertools
from itertools import permutations

primes = set()


def isPrime(n):
    if n == 1 or n == 0: return False
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0: return False

    return True


def search(s, num):
    global primes
    if num != '' and isPrime(int(num)):
        primes.add(int(num))

    for i in range(len(s)):
        search(s[:i] + s[i + 1:], num + s[i])


def solution(numbers):
    search(numbers, '')
    return len(primes)


if __name__ == '__main__':
    a = [1,2,3]
    per = itertools.combinations(a,2)
    for i in per :
        print(i)