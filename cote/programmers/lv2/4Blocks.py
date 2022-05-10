def check(a, b, c, d):
    return a == b and b == c and c == d and a != '-'


def solution(m, n, board):
    answer = 0
    newBoard = [[] for _ in range(m)]

    for i, line in enumerate(board):
        for c in line:
            newBoard[i].append(c)
    k = 1
    while True:
        k += 1
        popList = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if check(newBoard[i][j], newBoard[i + 1][j], newBoard[i][j + 1], newBoard[i + 1][j + 1]):
                    popList.update([(i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)])

        if not popList: break


        for i, j in popList:
            newBoard[i][j] = '-'
        print(newBoard)

        for _i in range(m-1,0,-1):
            for j in range(n):
                for i in range(_i-1,-1,-1):
                    if newBoard[_i][j] == '-' and newBoard[i][j] != '-':
                        newBoard[_i][j], newBoard[i][j] = newBoard[i][j], newBoard[_i][j]


        answer += len(popList)

        print(newBoard)

    return answer


print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))
