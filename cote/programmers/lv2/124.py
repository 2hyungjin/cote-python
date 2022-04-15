def solution(n):
    answer = ''
    while n>0:
        l = n % 3
        if l == 0 :
            answer+='4'
            n=n//3-1
        else :
            answer+=str(l)
            n//=3

    print(answer[::-1])
    return answer[::-1]