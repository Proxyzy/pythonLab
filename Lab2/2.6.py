inp = int(input())
if inp > 1:
    for i in range(2, int(inp / 2) + 1):
        if (inp % i) == 0:
            print("nepirminis")
            break
    else:
        print("pirminis")

else:
    print("nepirminis")