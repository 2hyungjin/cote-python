def solution(triangle):
    dp = [[0] * i for i in range(1, 501)]

    for i in range(len(triangle)):
        line = triangle[i]
        for n in range(len(line)):
            if n == 0:
                topLeft = 0
            else:
                topLeft = dp[i - 1][n - 1]
            if n == len(line) - 1:
                topRight = 0
            else:
                topRight = dp[i - 1][n]

            dp[i][n] = max(topLeft, topRight) + line[n]

    answer = max(dp[len(triangle) - 1])
    return answer