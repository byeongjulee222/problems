import sys; sys.stdin = open('txt/1149_RGB거리.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# i행에서 빨강(0), 초록(1), 파랑(2)을 선택했을 때 최소값을 그 자리에 저장
# 예) 1행에서 빨강(0)을 선택하면 0행에서 초록(1)이나 파랑(2)을 선택해야하는데
# 둘 중 작은것과 1행의 빨강(0)값을 더함 -> 1행 0열에 저장
for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    print(arr)
print(min(arr[N-1]))