inp = input()
new_line = ""
for element in range(0, len(inp), 2):
    if int(element) == 0:
        new_line = new_line + inp[element] * int(inp[element + 1])
    elif int(inp[element+1]) == 0:
        new_line += ""
    else:
        new_line = new_line + " " + inp[element] * int(inp[element + 1])
print(new_line)