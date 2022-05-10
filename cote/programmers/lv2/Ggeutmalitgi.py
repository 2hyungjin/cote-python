import math


def solution(n, words):
    answer = [0, 0]
    record = []
    temp = ""
    for i, word in enumerate(words):
        if i == 0:
            temp = word
            record.append(word)
            temp = word
            continue

        if temp[-1] != word[0] or word in record:
            r = math.ceil((i + 1) / n)
            p = i % n + 1
            return [p, r]

        record.append(word)
        temp = word

    return answer