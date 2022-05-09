import itertools


def solution(k, dungeons):
    max_value = 0
    stages = [i for i in range(len(dungeons))]
    case = set(itertools.permutations(stages))

    for c in case:
        piro = k
        count = 0
        for stage in c:
            if piro >= dungeons[stage][0]:
                piro -= dungeons[stage][1]
                count += 1
        max_value = max(count, max_value)

    return max_value
