n = int(input())
L1 = []
if n > 0:
    L1 = input().split()
L1 = [pow(int(i), 2) for i in L1]
print(L1)