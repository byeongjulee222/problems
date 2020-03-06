import sys; sys.stdin = open('txt/3752_가능한 시험 점수.txt', 'r')
from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    # nums = deque(map(int, input().split()))
    nums = list(map(int, input().split()))
    s = {0}
    while nums:
        tmp = nums.pop(0)
        ss = list(s)
        for i in ss:
            s.add(i+tmp)
    print('#{} {}'.format(tc, len(s)))


'''
N = int(input())
nums = list(map(int, input().split()))
candi = [1] + [0] * sum(nums)
ans = 0
for i in range(N):
    ans += nums[i]
    for j in range(ans, -1, -1):
        if candi[j]:
            candi[j+nums[i]] = 1

print('#{} {}'.format(tc, candi.count(1)))
'''
#
# T = int(input())
# for tc in range(1, T+1):
#     d = input()
#     data = map(int, input().split())
#     a = 1
#     for i in data:
#         # i번 비트를
#         a |= a<<i
#     print('#{} {}'.format(tc, bin(a).count('1')))

# for tc in range(1, int(input())+1):
#     N = int(input())
#     score = list(map(int, input().split()))
#     check = [1] + [0]*sum(score)
#     subsets = {0}
#     for j in score:
#         temp = set(subsets)
#         for t in temp:
#             if not check[t+j]:
#                 check[t+j] = 1
#                 subsets.add(t+j)
#     print('#{} {}'.format(tc, sum(check)))