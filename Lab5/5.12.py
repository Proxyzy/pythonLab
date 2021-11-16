inp = input()
inp = inp.split(' ')
ats = ""
for i in range(1, len(inp)):
    if int(inp[i]) > int(inp[i-1]):
        if ats == "":
            ats = ats + inp[i]
        else:
            ats = ats + " " + inp[i]
print(ats)