import sys; sys.stdin = open('txt/1018_체스판 다시 칠하기.txt', 'r')
from pprint import pprint
# 전체 판에서 8*8 크기로 잘라서
# 체스판을 만들 때 가장 적게 바꿀때의 횟수

A = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

# for tc in range(1, int(input())+1):
N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(input()))
c = 0
Min = 0xffffff
for a in range(N-7):
    for b in range(M-7):
        cnt_A, cnt_B = 0, 0
        for i in range(8):
            for j in range(8):
                if A[i][j] != arr[a+i][b+j]: cnt_A += 1
                if B[i][j] != arr[a+i][b+j]: cnt_B += 1
        # print('cnt_A :', cnt_A)
        # print('cnt_B :', cnt_B)
        # c += 1
        # print('c :', c)
        Min = min(cnt_A, cnt_B, Min)
        # print('Min :', Min)

print(Min)
# print('----------')
# break