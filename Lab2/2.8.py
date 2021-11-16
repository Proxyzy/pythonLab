import math


inp = int(input())
sum = 0
for i in range(1, inp+1):
    sum = sum + math.factorial(i)
print(sum)