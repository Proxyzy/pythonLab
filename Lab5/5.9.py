L = input().split()
n = int(input())
res = []
[res.append(x) for x in L if len(x) >= n]

if len(res) != 0:
    print(res)
else:
    print("Tokiu zodziu eiluteje nera")