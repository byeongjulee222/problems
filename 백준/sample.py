# 조합 생성
import itertools
N, R = 4, 2 # 0 ~ N - 1 중에 R 개를 선택

arr = itertools.combinations([i for i in range(N)], R)
for val in arr:
    print(val)


for i in range(N - 1):
    for j in range(i + 1, N):
        print(i, j)