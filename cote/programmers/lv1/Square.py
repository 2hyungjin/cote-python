def solution(sizes):
    height = [max(card) for card in sizes]
    width = [min(card) for card in sizes]

    return max(height) * max(width)