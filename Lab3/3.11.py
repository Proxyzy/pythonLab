inp = input()
letter = ""
count = 0
out = ""
for i in range(len(inp)):
    if letter == "" or letter == inp[i]:
        letter = inp[i]
        count = count + 1
    else:
        out = out + str(count) + letter + " "
        letter = inp[i]
        count = 1
out = out + str(count) + letter
print(out)