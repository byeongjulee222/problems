import sys; sys.stdin = open('txt/1018_체스판 다시 칠하기.txt', 'r')
from pprint import pprint
# 전체 판에서 8*8 크기로 잘라서
# 체스판을 만들 때 가장 적게 바꿀때의 횟수

def chess(a, b):
    pass

arr1 = [[1, 2, 3], [2, 3, 4]]
arr2 = [[1, 2, 3], [2, 3, 5]]

#
# for tc in range(1, int(input())+1):
#     N, M = map(int, input().split())
#
#     arr = []
#     for _ in range(N):
#         arr.append(list(input()))
#
#     for i in range(N):
#         for j in range(M):
#             Min = 0xffffff
#             for row in range(8):
#                 for col in range(8):
#                     pass
#
#     pprint(arr)
#     break

print(arr1 == arr2)