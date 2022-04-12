num, k = map(int, input().split())
count = 0
if __name__ == '__main__':

    # while num != 1:
    #     if num % k == 0:
    #         num //= k
    #     else:
    #         num -= 1
    #     count += 1
    # print(count)

    while num >= k:
        target = (num // k) * k
        count += num - target

        num = target // k
        count += 1
    count += num - 1
    print(count)
