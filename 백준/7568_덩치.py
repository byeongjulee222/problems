import sys; sys.stdin = open('txt/7568_덩치.txt', 'r')
# 단순히 한 명을 선택해서 배열을 도는데
# 키, 몸무게 다 크면 rank += 1

N = int(input())

arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

# print(arr)

for person in arr:
    rank = 1
    for compare in arr:
        if person[0] < compare[0] and person[1] < compare[1]:
            rank += 1
    print(rank, end=' ')