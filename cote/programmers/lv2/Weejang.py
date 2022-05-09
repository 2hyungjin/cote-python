def solution(clothes):
    answer = 1
    clothDict = dict()

    for cloth in clothes:
        name, category = cloth[0],cloth[1]

        clothDict[category]=clothDict.get(category,0)+1

    for v in clothDict.values():
        answer *= v+1


    return answer-1