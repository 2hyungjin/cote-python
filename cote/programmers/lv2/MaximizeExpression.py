import itertools


def calc(num1, num2, operation):
    if operation == '+': return num1 + num2
    if operation == '-': return num1 - num2
    if operation == '*': return num1 * num2


def solution(expression):
    numbers = []
    operations = []
    cases = set(itertools.permutations(['+', '*', '-']))
    temp = ""
    answer = 0

    for s in expression:
        if s.isdigit():
            temp += s
        else:
            numbers.append(int(temp))
            temp = ""
            operations.append(s)
    numbers.append(int(temp))

    for case in cases:
        _numbers = list(numbers)
        _operations = list(operations)

        for c in case:
            i = _operations.index(c) if c in _operations else -1

            while i != -1:
                _numbers[i] = calc(_numbers[i], _numbers[i + 1], c)
                _numbers.pop(i + 1)
                _operations.pop(i)

                i = _operations.index(c) if c in _operations else -1
        answer = max(answer, abs(_numbers[0]))

    return answer