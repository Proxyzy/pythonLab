inp = int(input())
d = []
for i in range(inp):
    a = input().split()
    d.append((' '.join(a[:-1]), int(a[-1])))
    print(d)

d.sort(key=lambda x: x[1], reverse=True)
print(d)