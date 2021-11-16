inp = int(input())
max1 = inp
max2 = 0
inp = int(input())
if(inp > max1):
    max2 = max1
    max1 = inp
else:
    max2 = inp
while inp != 0:
    if inp > max1:
        max2 = max1
        max1 = inp
    elif max2 < inp < max1:
        max2 = inp
    inp = int(input())
print(max2)