maze = []
n, m = 0, 0
result = 1e9


def dfs(count, row, col):
    global maze, result

    if row == n - 1 and col == m - 1:
        if result > count: result = count
        return

    if row < 0 or row >= n or col < 0 or col >= m: return

    if maze[row][col] == 0: return
    maze[row][col] = 0

    dfs(count + 1, row + 1, col)
    dfs(count + 1, row - 1, col)
    dfs(count + 1, row, col + 1)
    dfs(count + 1, row, col - 1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        maze.append(list(map(int, input())))

    dfs(1, 0, 0)
    print(result)
