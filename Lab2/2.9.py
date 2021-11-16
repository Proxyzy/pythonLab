import math
inp = int(input())

maxPow = 1
maxPowNumber = 0

while math.pow(2, maxPowNumber+1) <= inp:
    maxPow = math.pow(2, maxPowNumber+1)
    maxPowNumber = maxPowNumber+1
print(f"{int(maxPow)} {maxPowNumber}")