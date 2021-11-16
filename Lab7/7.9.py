d = eval(input())
ats = sorted(d.items(), key=lambda x: x[1])[:2]
print(ats)