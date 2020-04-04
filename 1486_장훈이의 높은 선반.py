import sys; sys.stdin = open('txt/1486_장훈이의 높은 선반.txt', 'r')

# 모든 경우를 다 result에 넣고 최소값을 출력
def find(height, num):
    # 선반높이보다 높으면 result에 넣음
    if height >= B:
        result.append(height)
    if num == N: return

    # 높이 더하고 진행
    find(height+arr[num], num+1)
    # 높이 더하지않고 진행
    find(height, num+1)


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    result = []
    find(0, 0)
    print('#{} {}'.format(tc, min(result)-B))