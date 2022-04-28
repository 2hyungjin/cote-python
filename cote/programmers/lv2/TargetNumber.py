count = 0
def calculate(num,result,operation,target):
    global count
    if operation : result += num[0]
    else : result -= num[0]

    if len(num)==1 :
        if result == target: count+=1
        return
    else :
        calculate(num[1:],result,True,target)
        calculate(num[1:],result,False,target)

def solution(numbers, target):
    global count

    calculate(numbers,0,True,target)
    calculate(numbers,0,False,target)

    return count