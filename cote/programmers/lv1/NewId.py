def solution(new_id):
    case = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    for i in range(0, 10): case.append(str(i))
    case.append("-")
    case.append("_")
    case.append(".")

    answer = ''.join([c for c in new_id.lower() if c in case])

    while '..' in answer:
        answer = answer.replace('..', '.')

    answer = answer.strip('.')

    if not answer : answer = 'a'

    if len(answer) >= 16: answer = answer[:15].strip('.')
    if len(answer) <= 2:
        while len(answer) < 3: answer += answer[-1]

    return answer

print(solution("=.="))