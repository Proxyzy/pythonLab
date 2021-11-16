inp = int(input())
numbers=[]
inp2 = input()
numbers = inp2.split(" ")
remove_number = input()
try:
    x = numbers.index(remove_number)
    del numbers[x]
    number_count = numbers.count(remove_number)
    print(f'Elemento "{remove_number}" indeksas - {x}\nElementas is pozicijos {x} pasalintas\nLiko "{remove_number}" elementu sarase - {number_count}')
except:
    print('Tokio elemento sarase nera')