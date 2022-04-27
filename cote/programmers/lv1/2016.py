def solution(a, b):
    total = 0
    days = ('FRI','SAT','SUN','MON','TUE','WED','THU')
    daysOfMonth = (31,29,31,30,31,30,31,31,30,31,30,31)

    for month in range(a-1): total+=daysOfMonth[month]
    total += b-1

    return days[total%len(days)]