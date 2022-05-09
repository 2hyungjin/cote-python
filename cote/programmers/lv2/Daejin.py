import math


def solution(n, a, b):
    aRecord = [-1]
    bRecord = [1e9]

    while n > 1:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)

        aRecord.append(a)
        bRecord.append(b)

        n //= 2

    for i, (a, b) in enumerate(zip(aRecord, bRecord)):
        if a == b: return i