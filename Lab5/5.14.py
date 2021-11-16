inp = int(input())
L = []
for i in range(inp):
    col = list(map(int, input().split(' ')))
    L.append(col)
switch = list(map(int, input().split(' ')))

for i in range(inp):
    place_holder = L[i][switch[0]-1], L[i][switch[1]-1]
    L[i][switch[1]-1], L[i][switch[0]-1] = place_holder
    print(L[i])