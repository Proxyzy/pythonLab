inp = input()
letter = ""
count = 0
out = ""
for i in range(len(inp)):
    if inp[i].isalpha():
        letter = inp[i]
        count = 0
        for y in range(len(inp)):
            if letter == inp[y]:
                inp = inp.replace(letter, "1", 1)
                count = count + 1
        if i == 0:
            out = out + str(count) + letter
        else:
            out = out + " " + str(count) + letter
print(out)