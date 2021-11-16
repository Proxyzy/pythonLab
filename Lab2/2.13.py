inp = int(input())
numberList = []
while inp != 0:
    numberList.append(inp)
    inp = int(input())

numberList.sort(reverse=True)
print(numberList.count(numberList[0]))