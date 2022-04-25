def solution(board, moves):
    board_horizontal = [[] for _ in board]
    count=0
    answer = []

    for line in board:
        for i,doll in enumerate(line):
            if doll != 0 :
                board_horizontal[i].append(doll)

    for move in moves:
        if board_horizontal[move-1]:
            doll = board_horizontal[move-1].pop(0)


            if answer:
                if answer[-1] == doll:
                    answer.pop()
                    count+=2
                else : answer.append(doll)
            else : answer.append(doll)


    answer = 0
    return count
