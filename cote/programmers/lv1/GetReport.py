def solution(id_list, report, k):
    answerList = []
    reports = dict()
    for id in id_list:
        answerList.append(0)
        reports[id] = set()

    for line in report:
        user = line.split(" ")[0]
        target = line.split(" ")[1]

        reports[target].add(user)

    for users in reports.values():
        if len(users) >= k:
            for user in users:
                answerList[id_list.index(user)] += 1

    return answerList