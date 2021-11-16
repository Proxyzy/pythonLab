l_count = 0
w_count = 0
s_count = 0
with open('../names.txt', 'r') as f:
    for line in f:
        line = line.strip("\n")
        l_count = l_count + 1
        w_count = w_count + len((line).split())
        line = line.replace(' ', '')
        s_count = s_count + len(line)
print(f"eiluciu - {l_count}\nzodziu - {w_count}\nsimboliu - {s_count}")