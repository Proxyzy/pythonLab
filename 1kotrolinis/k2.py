def Filtruoti(a, *x):
    list1 = list(map(int, list(a)+list(x)))
    print(list1)
    set1 = set(list1)
    print(set1)
    set2 = {x for x in set1 if x % int(a) == 0 and x % 2 != 0}
    return set2


a, b, *x = input().split()
aibe = Filtruoti(a, b, *x)
print(*sorted(aibe), sep=", ")