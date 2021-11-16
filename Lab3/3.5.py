inp = input()
if inp.find('a') > -1:
    inp = inp.replace('a', '1', 1)
    print(inp.find('a'))
else:
    print('-2')