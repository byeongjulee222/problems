import sys; sys.stdin = open('txt/1486_장훈이의 높은 선반.txt', 'r')

# 모든 경우의 가지치기를 해보고 최소값을 출력
def find(height, num):
    # 선반의 물건을 꺼낼 수 있는 높이라면 result에 추가
    if height >= B:
        result.append(height)
    if num == N: return

    # 더하고 진행
    find(height+arr[num], num+1)
    # 더하지 않고 진행
    find(height, num+1)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    find(0, 0)
    print('#{} {}'.format(tc, min(result)-B))