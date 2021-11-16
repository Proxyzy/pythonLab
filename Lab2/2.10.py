
inp = int(input())

for i in range(2, abs(inp)+1):
    if inp % i == 0:
        print(i)
        break