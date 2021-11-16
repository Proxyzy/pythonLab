key = 0
value = 0
dictionary = dict()
while True:
    key, value = input().split()
    if key == 'q' and value == 'q':
        break
    dict.update({key: int(value)})
if len(dict) > 0:
    print(max(dict, key=lambda x: dict[x]))
print(dict)