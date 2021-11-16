f = open('../lines.txt', 'w')
while True:
    try:
        line = input()
        f.write(line+"\n")
    except:
        break
f.close()
