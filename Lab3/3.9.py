inp = input()
i = inp.find('Python')
while i != -1:
    last_instance = i
    inp = inp.replace('Python', 'xxxxxx', 1)
    i = inp.find('Python')
print(last_instance)