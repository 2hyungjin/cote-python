def solution(record):
    uidDict = dict()
    result = []
    for r in record:
        command, uid = r.split()[0], r.split()[1]

        if command == 'Leave':
            result.append((uid, "님이 나갔습니다."))
        else:
            command, uid, nickname = r.split(' ')
            uidDict[uid] = nickname
        if command == 'Enter': result.append((uid, "님이 들어왔습니다."))

    answer = map(result, lambda r: uidDict[r[0]] + r[1])

    return []
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])