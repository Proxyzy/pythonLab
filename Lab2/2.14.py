inp = int(input())
n1, n2 = 0, 1
count = 0
if inp == 0:
    print(n1)
elif inp == 1:
    print(n2)
else:
    while count < inp:
        print(n1)
        new = n1 + n2
        n1 = n2
        n2 = new
        count = count + 1
    print(n1)