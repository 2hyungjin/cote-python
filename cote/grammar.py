a = 4.
b = 3

li = []
li.append(1)

li = [[0] * 3 for _ in range(2)]

tuple = (1, 2, 3)

dic = dict()

dic[1] = 2
dic[2] = 3

dic = {
    1: 2,
    2: 3,
    3: 4
}

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(2 in tuple)

print(list(dic.values()))
print()
print(3 in set1)

print(list(set1 & set2))


def fun():
    print(a)
