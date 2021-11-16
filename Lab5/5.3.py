n = int(input())
if n > 0:
    L1 = input()
m = int(input())
if m > 0:
    L2 = input()
L3 = []
if n != 0 and m != 0:
    L1 = L1.split(' ')
    L2 = L2.split(' ')
    for i in range(len(L1)):
        L3.append(L1[i]+L2[i])
    print(L3)
else:
    print(L3)