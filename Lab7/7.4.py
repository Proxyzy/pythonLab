inp = eval(input())
inp.update(eval(input()))

L = list(inp.items())

L.sort(key=lambda x: x[1])
for a, b in L:
    print(f'{a} - {b}')