def solution(nums):
    size = len(nums)
    pokemons = len(set(nums))

    return min(size//2,pokemons)