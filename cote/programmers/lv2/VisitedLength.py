def solution(dirs):
    nx = [0,0,1,-1]
    ny = [1,-1,0,0]
    UDRL = ['U','D','R','L']
    now = (0,0)
    moves  = set()

    for d in dirs:
        x,y = now
        _x,_y = x+nx[UDRL.index(d)], y+ny[UDRL.index(d)]

        if -5<=_x<=5 and -5<=_y<=5:
            if x+y>_x+_y : move = f"{x}{y}{_x}{_y}"
            else : move = f"{_x}{_y}{x}{y}"
            now = (_x,_y)
            moves.add(move)
    print(moves)
    return len(moves)