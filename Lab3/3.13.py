inp = input()
symbol = ""
out = ""
while inp != "":
    symbol = inp[0]
    inp = inp.replace(symbol, '')
    out = out + symbol
print(out)