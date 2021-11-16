inp = int(input())
for i in range(1, inp+1):
    j = 0
    for j in range(i):
        if j < i - 1:
            print(i, end=" ")
        else:
            print(i)