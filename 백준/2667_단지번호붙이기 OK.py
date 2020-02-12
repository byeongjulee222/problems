import sys; sys.stdin = open("txt/bj_2667.txt", "r")
# DFS (1)
# result 리스트를 만들어서 단지 수 추가
# len(result) 출력하고
# result 를 오름차순 정렬한 후 print

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def dfs(x, y):
    global cnt
    # 방문했으면 그 지점은 0으로 변경
    arr[x][y] = 0
    visit[x][y] = True
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        # 경계조건 + 방문조건 + 맵에서의 위치 값 == 1
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and arr[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny)
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
# print(arr)

visit = [[False]*N for _ in range(N)]
res = []
# 1인 지점을 만났을 때 그 지점을 개수에 포함시켜야 하므로
# cnt = 1로 시작한다.
cnt = 1
for i in range(N):
    for j in range(N):
        # 맵은 하나로 고정 되어있기 때문에
        # not visit으로 끊어낼 수 있다
        if arr[i][j] == 1 and not visit[i][j]:
            dfs(i, j)
            res.append(cnt)
            cnt = 1

# .sort()는 변경사항이 저장됨
res.sort()
print(len(res))
for i in res:
    print(i)