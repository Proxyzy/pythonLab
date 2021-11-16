for i in range(4):
    try:
        inp = int(input())
        if inp not in range(101):
            print("Ne visi ivesti skaiciai priklauso intervalui [0;100]")
            break
    except:
        pass
else:
    print("Visi ivesti skaiciai priklauso intervalui [0;100]")