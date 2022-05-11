def solution(skill, skill_trees):
    answer = 0
    _skill_list = [c for c in skill]

    for skill_tree in skill_trees:
        skill_list = list(_skill_list)
        is_it_ok = True

        for skill in skill_tree:
            if skill in skill_list:
                if skill == skill_list[0]:
                    skill_list.pop(0)
                else:
                    is_it_ok = False
        if is_it_ok: answer += 1

    return answer