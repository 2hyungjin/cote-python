def solution(s):
    zeros = 0
    count = 0
    while int(s) != 1:
        count += 1
        zeros += s.count('0')

        s = bin(len(s.replace('0', '')))[2:]

    return [count, zeros]