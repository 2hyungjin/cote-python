def solution(msg):
    alphabet = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = [c for c in alphabet]
    answer = []
    new = ""
    i = 0

    while i < len(msg):
        new = new + msg[i]
        if new not in dic:
            dic.append(new)
            answer.append(dic.index(new[:-1]))
            new = new[-1]

        i += 1

    answer.append(dic.index(new))

    return answer