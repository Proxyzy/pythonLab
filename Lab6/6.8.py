L1 = map(int, input().split())
L2 = map(int, input().split())
answer = set(L1) & set(L2)

print(f"{len(answer)}\n{sorted(answer)}")