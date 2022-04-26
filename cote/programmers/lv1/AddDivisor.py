def getDivisor(num):
    answer=set()
    if num == 1 : return 1
    for i in range(1,int(num**1/2)+1):
        if num % i == 0 :
            answer.add(i)
            answer.add(num//i)
    return len(answer)

def solution(left, right):
    answer=0
    for n in range(left,right+1):
        if getDivisor(n) % 2 == 0: answer+=n
        else : answer-=n
    return answer