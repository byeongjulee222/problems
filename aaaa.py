H, M = map(int, input().split())
total = H*60 + M - 45
a = total//60 if total//60 >= 0 else 23
print(a, total%60, end=' ')
