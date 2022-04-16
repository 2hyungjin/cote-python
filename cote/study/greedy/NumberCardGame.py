def solution(cards):
    firsts=[]
    for card in cards:
        firsts.append( min(card))
    return max(firsts)

if __name__ == '__main__':
    n,m = map(int,input().split())
    list = []
    for i in range(n):
        list.append(map(int,input().split()))
    print(solution(list))
