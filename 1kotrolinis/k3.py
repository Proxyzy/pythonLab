def Funkcija(set1, set2):
    set3 = set2.intersection(set1)
    print(sorted(set3) if set3 else "no")
    if set1.issubset(set2):
        print("yes")
    elif set2.issubset(set1):
        print("yes")
    else:
        print("no")
    return max(set3), min(set3)





set1 = eval(input())
set2 = eval(input())
a, b = Funkcija(set1, set2)
print(pow(b, a))