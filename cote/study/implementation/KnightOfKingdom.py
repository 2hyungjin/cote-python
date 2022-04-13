if __name__ == '__main__':
    directions = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    input = input()

    count = 0

    x = directions.index(input[0])
    y = int(input[1]) - 1

    print(x,y)
    dx = [-2, -2, 2, 2, -1, 1, -1, 1]
    dy = [1, -1, 1, -1, 2, 2, -2, -2]

    for i in range(8):
        _x = dx[i] + x
        _y = dy[i] + y

        print(_x,_y)

        if 0 <= _x <= 7 and 0 <= _y <= 7: count += 1
    print(count)
