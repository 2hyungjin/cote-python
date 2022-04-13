n, m = 0, 0
graph = []


def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= m: return False
    if graph[row][col] == 0:
        graph[row][col] = 1
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        return True
    return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        graph.append(list(map(int, input())))


    result = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j): result += 1
    print(result)
