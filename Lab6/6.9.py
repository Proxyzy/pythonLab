word = set(input().lower())
vowel = set('aeiyou')
print(tuple(sorted(word.difference(vowel))))
