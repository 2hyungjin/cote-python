if __name__ == '__main__':
    x, y = 1, 1
    n = int(input())
    directions = list(input().split())

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for d in directions:
        if d == 'R':
            x = x + dx[0]
            y = y + dy[0]
        if d == 'L':
            x = x + dx[1]
            y = y + dy[1]
        if d == 'U':
            x = x + dx[2]
            y = y + dy[2]
        if d == 'D':
            x = x + dx[3]
            y = y + dy[3]

        if x < 1: x = 1
        if y < 1: y = 1
        if x > 5: x = 5
        if y > 5: y = 5

    print(x, y)
