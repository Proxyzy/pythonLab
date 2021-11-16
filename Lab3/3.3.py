inp = input()
inp2 = input()
length = int(len(inp))
half = int(length/2)
beginning = inp[:half]
end = inp[half:]
new_string = beginning + inp2 + end
print(new_string)