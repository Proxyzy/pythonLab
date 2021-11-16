inp = eval(input())
a, b = input().split()
temp = []
for i in inp:
    if type(i) == list:
        temp = i
try:
    temp[temp.index(int(a))] = int(b)
except:
    pass
finally:
    print(inp)

