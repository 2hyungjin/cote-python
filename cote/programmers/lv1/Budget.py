def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        budget-=i
        if budget<0: return answer
        answer+=1
    return answer