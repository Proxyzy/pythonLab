zodynas = eval(input())
vardas = input()
reiksme = input()

for i in zodynas.values():
    if i['name'] == vardas:
        i['salary'] = int(reiksme)
print(zodynas)