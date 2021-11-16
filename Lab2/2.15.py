inp = input()
inp2 = input()
maximum = 0
minimum = 0
if int(inp) > int(inp2):
    maximum = int(inp)
    minimum = int(inp2)
else:
    maximum = int(inp2)
    minimum = int(inp)
while inp != "x":
    if maximum < int(inp):
        maximum = int(inp)
    if minimum > int(inp):
        minimum = int(inp)
    inp = input()
if maximum == minimum:
    print(maximum)
else:
    print(f'{minimum} {maximum}')
