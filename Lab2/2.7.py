inp1 = int(input())
inp2 = int(input())
count = 0
for num in range(inp1, inp2 + 1):
    if num > 1:
        for i in range(2, int(num/2+1)):
            if (num % i) == 0:
                break
        else:
            print(num)
            count = count + 1
print(count)