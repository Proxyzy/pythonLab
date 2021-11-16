S = set()
with open("../text.txt", 'r') as f:
    text = ''.join(f.readlines()).lower().split()
    S = {x: text.count(x) for x in text}
    print(list(S.values()).count(1))
    for word, count in S.items():
        if int(count) == 1:
            print(word)
