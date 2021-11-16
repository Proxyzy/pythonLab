inp = input()
inp = inp.lower()
count = 0
i = inp.find('lt')
while i != -1:
    count = count + 1
    inp = inp.replace('lt', 'xx', 1)
    i = inp.find('lt')
print(count)
