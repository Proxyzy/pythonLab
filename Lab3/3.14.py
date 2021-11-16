inp1 = input()
inp2 = input()

inp1 = inp1.replace(" ", "")
inp2 = inp2.replace(" ", "")
inp1 = inp1.lower()
inp2 = inp2.lower()
leng = 0

if len(inp1) == len(inp2):
    for i in range(len(inp1)):
        for j in range(len(inp1)):
            if(inp1[i] == inp2[j]):
                inp1 = inp1.replace(inp2[j], "1", 1)
                leng = leng + 1
if leng == len(inp1):
    print("TAIP")
else:
    print("NE")