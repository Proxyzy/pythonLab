inp = int(input())
evenCount = 0
while inp != 0:
    if inp % 2 == 0:
        evenCount = evenCount + 1
    inp = int(input())
print(evenCount)