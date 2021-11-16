inp = input()
num = []
alp = []
for sub in inp:
    if sub.isnumeric():
        num.append(sub)
    else:
        alp.append(sub)
inp = sorted(alp) + sorted(num)
print(''.join(inp))