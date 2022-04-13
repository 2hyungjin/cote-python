def solution(number, k):
    count = k
    flag = True

    while flag:
        for i in range(len(number) - 1):
            if number[i] == 9: continue

            if number[i] < number[i + 1]:
                number = number[:i] + number[i + 1:]
                count -= 1
                break

            if i == len(number) - 2: flag = False
        if count <= 0: flag = False

    return number[:len(number) - count]