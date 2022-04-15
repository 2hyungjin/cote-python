def solution(s):

    stack=[s[0]]

    for i in range(1,len(s)):
        if len(stack)>0 :
            if s[i] == stack[-1]:
                stack.pop()
            else : stack.append(s[i])
        else : stack.append(s[i])


    if len(stack)>0 : return 0
    return 1