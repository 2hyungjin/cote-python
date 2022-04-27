def solution(n, arr1, arr2):
    map1 = [[] for i in range(n)]
    map2 = [[] for i in range(n)]
    answer = [[] for i in range(n)]

    for i, (row1, row2) in enumerate(zip(arr1, arr2)):
        decode1 = bin(row1)[2:].zfill(n)
        decode2 = bin(row2)[2:].zfill(n)

        for j in decode1:
            map1[i].append(int(j))
        for j in decode2:
            map2[i].append(int(j))


    for i in range(n):
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                answer[i].append('#')
            else:
                answer[i].append(' ')

    return answer