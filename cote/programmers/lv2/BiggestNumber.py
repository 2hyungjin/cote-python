import functools
def compare(a,b):
    if str(a)+str(b) > str(b)+str(a) : return 1
    else : return -1

def solution(numbers):
    numbers.sort(key = functools.cmp_to_key(compare), reverse = True)
    return str(int(''.join(map(str,numbers))))