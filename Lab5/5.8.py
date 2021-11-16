L = eval(input())
res = []
[res.append(x) for x in L if x not in res]
print(res)