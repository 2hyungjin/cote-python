def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    while len(people) > 0:
        first = people[0]
        if len(people)>2 :
            last = people[len(people) - 1]

            if first + last <= limit: people.remove(last)
        people.remove(first)
        answer+=1

    return answer


if __name__ == '__main__':
    print(solution([10, 20, 30, 40, 50, 60, 70, 80, 90], 100))
