minLength = 1e9


def zip(s, n):
    global minLength
    temp = ""
    newS = ""
    count = 1
    while s:
        temp = s[:n]
        s = s[n:]
        if temp == s[:n]:
            count += 1
        else:
            if count > 1: newS += str(count)
            newS += temp
            count = 1

    minLength = min(minLength, len(newS))


def solution(s):
    global minLength
    minLength = len(s)

    for i in range(1, len(s) // 2 + 1):
        zip(s, i)

    return minLength

