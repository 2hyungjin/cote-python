n, m = 0, 0
array = []
answer = 0


def search(start, end):
    global answer, n, m, array
    print(start,end,answer)
    if start > end: return

    total = 0
    mid = (start + end) // 2

    for i in array:
        if i > mid: total += i - mid
    
    if total < m:
        search(start, mid-1)
    else:
        answer = mid
        search(mid+1, end)


if __name__ == '__main__':
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    search(0, max(array))
    print(answer)
