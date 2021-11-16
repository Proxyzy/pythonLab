inp = int(input())
L = []
for i in range(inp):
    col = list(map(int, input().split(' ')))
    L.append(col)
for i in range(len(L)):
    print(f"{i+1} eilute: min: {min(L[i])}, max: {max(L[i])}")