import sys; sys.stdin=open('txt/2382_미생물 격리.txt', 'r')



# 상 하 좌 우
dir = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())

    # 세로, 가로, 미생물 수, 방향
    bugs = [list(map(int, input().split())) for _ in range(K)]

