def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0] * 3

    for num in range(len(answers)):
        if answers[num] == a[num % len(a)]: scores[0] += 1
        if answers[num] == b[num % len(b)]: scores[1] += 1
        if answers[num] == c[num % len(c)]: scores[2] += 1

    score = max(scores)

    return [i + 1 for i in range(len(scores)) if scores[i] == score]