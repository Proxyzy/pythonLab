def append(array, search, add):
    for i, value in enumerate(array):
        if type(value) == list:
            append(value, search, add)
        elif int(value) == search:
            array.insert(i + 1, add)
    return array

L = eval(input())
a = int(input())
b = int(input())
print(append(L, a, b))