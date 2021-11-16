inp = input().split()
ats = set(inp)
if list(sorted(ats)) == sorted(inp):
    print('Visi sekos skaiciai yra unikalus')
else:
    print('Ne visi sekos skaiciai yra unikalus')