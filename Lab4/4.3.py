l_count = 0
s_count = 0
with open('../names.txt', 'r') as f:
    for line in f:
        l_count = l_count + 1
        if(l_count<=6):
            line = line.strip("\n").replace(" ", "")
            s_count = s_count + len(line)
        elif(l_count == 7):
            print(s_count)
            print(line.replace("\n", ""))
        else:
            print(line.replace("\n", ""))