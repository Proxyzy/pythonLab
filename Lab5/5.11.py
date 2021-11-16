inp = eval(input())
minimum = min(inp)
while minimum in inp:
    if minimum == min(inp):
        inp.remove(minimum)
minimum = min(inp)
print(minimum)