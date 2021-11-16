inp = input()
i = 0
flip = []
while i < len(inp):
    flip.insert(0, inp[i])
    i = i + 1
flip = ''.join(flip)
print(flip)