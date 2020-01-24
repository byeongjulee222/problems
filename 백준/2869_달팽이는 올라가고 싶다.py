# A : 올라가는 높이
# B : 미끄러지는 길이
# V : 나무의 높이

A, B, V = map(int, input().split())
day = 1
h = 0
while h < V:
    h += A
    if h >= V: break
    h -= B
    day += 1
    # print(h)
print(day)
print((V-B-1)//(A-B) +1)
if (V-A)%(A-B):
    print((V-A)//(A-B)+2)
else:
    print((V-A)//(A-B)+1)