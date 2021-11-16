inp = int(input())
numbers=[]
inp2 = input()
numbers = inp2.split(" ")
remove_number = input()
number_count = numbers.count(remove_number)
if number_count > 0:
    for i in range(0, number_count):
        x = numbers.index(remove_number)
        del numbers[x]
    print(f"{[int(x) for x in numbers]}\n{number_count}")
else:
    print('Tokio elemento sarase nera')