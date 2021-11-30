f = open('duom.txt', 'r')
list1 = list(map(int, f.readline().split()))
list2 = list(map(int, f.readline().split()))
print(list1)
print(list2)

list3 = list1 + list(map(lambda x: x*3, list2))
dict1 = {x: list3.count(x) for x in list3}
print(*list(filter(lambda x:x[1]>=3, dict1.items())), sep=", ")

print(max(dict1, key=lambda x: dict1[x]))

print(*sorted(dict1.items(), key= lambda x: (-x[1], x[0])))
