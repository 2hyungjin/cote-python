import itertools, collections


def solution(info, query):
    result = collections.defaultdict(list)
    answer = []

    for i in info:
        lan, job, career, food, grade = i.split()

        for case in itertools.product([lan, '-'], [job, '-'], [career, '-'], [food, '-']):
            result[''.join(case)].append(int(grade))

    for q in query:
        q = q.replace('and', '').replace('  ', ' ')
        lan, job, career, food, grade = q.split()

        answer.append(len([i for i in result[lan + job + career + food] if i >= int(grade)]))

    return answer