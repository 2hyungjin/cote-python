def solution(dartResult):
    bonusList = [0, 'S', 'D', 'T']

    points = [0]
    index = 0

    dartResult += "0S"

    zeroCheck = False

    for i, c in enumerate(dartResult):
        if c.isdigit():
            if zeroCheck: continue
            index += 1

            now = int(c)

            if dartResult[i + 1] == '0': now = 10

            points.append(now)
            zeroCheck = True

        elif c.isalpha():
            points[index] **= bonusList.index(c)
            zeroCheck = False
        else:
            if c == '*':
                points[index - 1] *= 2
                points[index] *= 2
            if c == '#':
                points[index] *= -1
            zeroCheck = False

    return sum(points)