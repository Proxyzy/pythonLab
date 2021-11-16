vowels = set('euioay')
dictionary = {}
text = input()
for letter in text:
    if letter in vowels:
        if letter in dictionary:
            dictionary[letter] = dictionary[letter] + 1
        else:
            dictionary[letter] = 1
print(dictionary)

