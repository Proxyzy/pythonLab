inp = input()
lower_count = 0
upper_count = 0
number_count = 0
special_count = 0
for i in inp:
    if i.islower():
        lower_count = lower_count + 1
    elif i.isupper():
        upper_count = upper_count + 1
    elif i.isnumeric():
        number_count = number_count + 1
    else:
        special_count = special_count + 1
print(f"Mazuju raidziu: {lower_count}\nDidziuju raidziu: {upper_count}\nSkaitmenu: {number_count}\nSpecialiuju simboliu: {special_count}")