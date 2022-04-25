def solution(lottos, win_nums):
    nums = [i for i in lottos if i in win_nums]
    answer = 7-len(nums)
    best = 7-(lottos.count(0)+len(nums))
    if answer == 7 : answer = 6
    if best == 7 : best = 6

    return [best,answer]