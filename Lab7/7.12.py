inp = input()
words = inp.split(" ")
dictionary = {}
max_dictionary = {}
for word in words:
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1
max_key, max_value = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0]
for k, v in dictionary.items():
    if v == max_value:
        max_dictionary.update({k: v})
print(dictionary)
print(max_dictionary)