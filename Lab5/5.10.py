inp = int(input())
rez = []
while inp > 1:
    for i in range(2, inp + 1):
        if inp % i == 0:
            rez.append(i)
            inp = int(inp / i)
            print(inp)
            break
print(rez)