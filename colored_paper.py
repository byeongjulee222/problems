import sys
sys.stdin = open('colored_paper.txt', 'r')

N = int(input())
# 범위 : 가로, 세로 최대 101칸의 정사각형
square = [[0] * 101 for _ in range(101)]

# 색종이 장 수만큼 반복
for n in range(1, N+1):
    # 시작점(a, b), 가로 너비, 세로 너비
    arr, b, c, d = list(map(int, input().split()))
    # 첫 번째 색종이 += 1, 두 번째 색종이 += 2, ...
    for i in range(c):
        for j in range(d):
            square[arr + i][b + j] = n

# 결과값을 저장할 리스트 만들기
result = [0] * N
for num in square:
    for foll in num:
        # 사각형 중 그 값에 해당하는 값이 있으면 결과값 리스트에 저장
        if foll:
            result[foll-1] += 1

for i in range(len(result)):
    print(result[i])