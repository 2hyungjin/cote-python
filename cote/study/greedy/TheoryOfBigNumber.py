def solution(n, m, k):
    answer = 0
    times = 0
    count = 0
    while count < m:
        print(answer)
        if times < k:
            answer += n[0]
            times+=1
        else:
            answer += n[1]
            times = 0
        count += 1
    return answer

if __name__ == '__main__':
    n,m,k = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort(reverse=True)
    print(solution(array,m,k))
