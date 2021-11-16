inp1 = input()
inp2 = input()
inp3 = input()

lengths = [len(inp1), len(inp2), len(inp3)]

max_length = max(lengths)
out = ""

for i in range(max_length):
    out = ""
    if i < lengths[0]:
        out = out + inp1[i]
    if i < lengths[1]:
        out = out + inp2[i]
    if i < lengths[2]:
        out = out + inp3[i]
    print(out)

