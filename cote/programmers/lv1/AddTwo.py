import itertools


def solution(numbers):
    return sorted(list(set(map(sum, set(itertools.combinations(numbers, 2))))))
