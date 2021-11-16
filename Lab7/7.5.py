empl = eval(input())
defaults = eval(input())

ats = dict.fromkeys(empl, defaults)
for a, b in ats.items():
    print(f"{a}: {b}")