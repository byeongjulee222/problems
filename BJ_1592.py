import sys; sys.stdin = open("txt/BJ_1592.txt", "r")

N, M, L = map(int, input().split())

# print(N, M, L)

# 스택에 0 리스트 만들고
# 공 받을때마다 += 1
# 스택의 값 중 L과 같은 값이 있다면
# 스택의 요소의 합 -1을 출력

cnt = [0 for _ in range(N+1)]
S = []
S.append(1)
while S:
    a = S.pop(0)
    if cnt[a] % 2:
        S.append(a+2)
        cnt[a+2] += 1
        b = S.pop(0)
    else:
        S.append(a-2)
    S.append()



print(cnt)