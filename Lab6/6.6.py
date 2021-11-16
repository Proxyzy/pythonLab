inp = eval(input())
alphaSet = set()
numericSet = set()
for i in inp:
    if i.isalpha():
        alphaSet.add(i)
    else:
        numericSet.add(int(i))

if len(alphaSet)>0:
    print(sorted(alphaSet))
if len(numericSet)>0:
    print(sorted(numericSet))