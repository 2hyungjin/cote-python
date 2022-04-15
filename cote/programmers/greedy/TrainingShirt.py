def solution(n, lost, reserve):
    lost.sort()

    lostList = [i for i in lost if i not in reserve]
    reserveList = [i for i in reserve if i not in lost]

    count = len(lostList)

    for i in lostList:
        if i - 1 in reserveList:
            reserveList.remove(i - 1)
            count -= 1
        elif i + 1 in reserveList:
            reserveList.remove(i + 1)
            count -= 1
    return n - count

