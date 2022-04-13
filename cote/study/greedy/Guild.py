if __name__ == '__main__':
    n = int(input())
    user = list(map(int, input().split()))
    user.sort()
    result = 0
    count = 0

    for i in user:
        count += 1
        if count == i:
            result += 1
            count = 0
    print(result)
