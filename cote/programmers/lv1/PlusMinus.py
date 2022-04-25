def getRealNumber(num, sign):
    if sign:
        return num
    else:
        return num * -1


def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)):
        answer += getRealNumber(absolutes[i], signs[i])
    return answer