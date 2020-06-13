import sys
sys.stdin = open("kill_fly.txt", "r")

R = int(input()) # 반복 횟수
for r in range(R):
    N,M = map(int, input().split())

    puzzle = [] # 2차원 리스트로 받아오기 위한 작업
    for _ in range(N):  # N x N 행렬에서 N개의 행에 값을 입력
        puzzle.append(input().split())

    MAX, result_list = 0, []
    for l in range(N-M+1):  # 열을 이동시키며 합을 구한 후 다음 행으로 넘어가기 위한 작업
        for i in range(N-M+1):  # 열을 이동시키며 합을 구하기 위한 작업
            num_list = []   # 각 사각형별 합을 구하기 위해 빈 리스트를 만듦
            for j in range(M):  # M x M 사각형 중 열 값을 나타냄
                for k in range(M):  # M x M 사각형 중 행 값을 나타냄
                    num_list.append(puzzle[j+l][k+i]) # 각 행, 열 값을 이동시키며 구역을 정함
                if MAX < sum(map(int, num_list)):   # 숫자 리스트의 합을 구하여 크기 비교 후 MAX 값 설정
                    MAX = sum(map(int, num_list))

    print('#{} {}'.format(r+1,MAX))