# 조합 생성
import itertools
N, R = 4, 3 # 0 ~ N - 1 중에 R 개를 선택

arr = itertools.combinations([i for i in range(N)], R)
for val in arr:
    print(val)


for i in range(N - 1):
    for j in range(i + 1, N):
        print(i, j)


sel = []
def backtrack(k, s):  # k : 고른 개수, 호출 depth
    if k == R:        # s : 반복의 시작, 이전에 고른 요소의 다음
        print(sel)
        return

    for i in range(s, N):
        # i 번을 고른다 --> 어딘가에 저장
        sel.append(i)
        backtrack(k + 1, i + 1)
        sel.pop()

backtrack(0, 0)