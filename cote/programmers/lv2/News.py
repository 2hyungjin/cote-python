def solution(str1, str2):
    case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str1 = str1.upper()
    str2 = str2.upper()
    list1 = [str1[i] + str1[i + 1] for i in range(0, len(str1) - 1) if str1[i] in case and str1[i + 1] in case]
    list2 = [str2[i] + str2[i + 1] for i in range(0, len(str2) - 1) if str2[i] in case and str2[i + 1] in case]

    union = []
    relative = []

    for s in list1:
        union.append(s)
        if s in list2:
            relative.append(s)
            list2.remove(s)

    union.extend(list2)

    if not relative: return 65536

    return int(len(relative) / len(union) * 65536)

print(solution("A+C","DEF"))
print(0/6)