from collections import deque


def solution(progresses, speeds):
    works = deque(progresses)
    times = deque(speeds)
    answer = []

    while works:
        count = 1
        days = round((100 - works.popleft())/times.popleft())


        for i, p in enumerate(works):
            works[i] = p + (times[i] * days)

        while len(works) > 0 and works[0] >= 100:
            works.popleft()
            times.popleft()
            count += 1

        answer.append(count)
    return answer

print(solution([2, 2, 1, 2],[1, 1, 1, 1]))
