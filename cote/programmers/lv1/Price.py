def solution(price, money, count):
    answer = sum(range(1,count+1)) * price - money
    if answer < 0 : return 0
    else : return answer